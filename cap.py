import cv2

# 打開攝像頭
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

 # 嘗試設置分辨率
width = 1280
height = 720
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
# 獲取實際設置的分辨率
actual_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
actual_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

if actual_width == width and actual_height == height:
    print(f"Resolution {width}x{height} is supported")
else:
    print(f"Resolution {width}x{height} is not supported")
    print(f"Actual resolution: {int(actual_width)}x{int(actual_height)}")

cap.release()
