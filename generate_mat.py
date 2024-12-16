import cv2
import numpy as np
import scipy.io
import yaml
import glob

def generate_calibration_files(image_path, chessboard_grid_size, screen_size, output_path="./"):
    """
    生成相機校準和屏幕相關的三個文件：
    - Camera.mat
    - screenSize.mat
    - monitorPose.mat
    """

    # 棋盤格內角點數量
    x, y = chessboard_grid_size

    # termination criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    # prepare object points
    objp = np.zeros((y * x, 3), np.float32)
    objp[:, :2] = np.mgrid[0:x, 0:y].T.reshape(-1, 2)

    objpoints = []  # 3D 點
    imgpoints = []  # 2D 點

    images = glob.glob(f"{image_path}/*.png")
    for fname in images:
        img = cv2.imread(fname)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        ret, corners = cv2.findChessboardCorners(gray, (x, y), None)
        if ret:
            objpoints.append(objp)
            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            imgpoints.append(corners2)

    # Camera Calibration
    ret, cameraMatrix, distCoeffs, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
    
    # Save Camera.mat
    scipy.io.savemat(f"{output_path}/Camera.mat", {"cameraMatrix": cameraMatrix, "distCoeffs": distCoeffs})
    print("Camera calibration saved to Camera.mat")

    # Save screenSize.mat
    scipy.io.savemat(f"{output_path}/screenSize.mat", screen_size)
    print("Screen size saved to screenSize.mat")

    # Solve Monitor Pose
    ret, rvec, tvec = cv2.solvePnP(objpoints[0], imgpoints[0], cameraMatrix, distCoeffs)
    rotation_matrix, _ = cv2.Rodrigues(rvec)
    scipy.io.savemat(f"{output_path}/monitorPose.mat", {"rotation_matrix": rotation_matrix, "translation_vector": tvec})
    print("Monitor pose saved to monitorPose.mat")

# 示例執行
screen_size = {"width_pixel": 1280, "height_pixel": 720}
generate_calibration_files(
    image_path="./calibration_images",
    chessboard_grid_size=(9, 6),
    screen_size=screen_size,
    output_path="./output_mat"
)
