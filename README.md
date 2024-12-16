# (前置作業)測試功能是否正常
1. 請先安裝所需套件(於requirements.txt) `pip install -r requirements.txt`
2. 測試cv2是否可讀取圖片(並出現於螢幕上) `python test.py`
3. 測試攝影機是否正常(並可於螢幕出現) `python test_cam.py`
4. 測試是否可設置分辨率 `python cap.py`
5. 測試設置+獲取幀率 `python cap2.py`

# (校正相機)
1. 請先下載[棋盤校正]並列印(https://raw.githubusercontent.com/opencv/opencv/master/doc/pattern.png)  
2. 校正程式 run `camera_calibration.py`  
3. 輸出需校正靜態圖片 run `ffmpeg -i {影片名稱}.mp4 -f image2 frames/video_01-%07d.png`  
4. 產生 run `camera_calibration.py`中的calibration function，請先調整chessboard_grid_size(9,6) 產生 `calibration_matrix.yaml`檔案

# Collect Training and Calibration Data for Gaze Tracking

This tool allows collecting gaze data necessary for personal calibration or training of eye-tracking models. It was developed as part of my master's thesis on [eye tracking with a monocular webcam](https://github.com/pperle/gaze-tracking).
The [framework for the full gaze tracking pipeline](https://github.com/pperle/gaze-tracking-pipeline) is also available.

The output is a folder with a CSV file containing the target that the person is looking at in pixels and the file name of the associated webcam image. For good calibration results, it is recommended to take at least 9 calibration images, the more, the better.

## How to run

1. `pip install -r requirements.txt`
2. If necessary, calibrate the camera using the provided interactive script `python calibrate_camera.py`, see [Camera Calibration by OpenCV](https://docs.opencv.org/4.5.3/dc/dbb/tutorial_py_calibration.html).>>這個要先跑起來確認攝影機沒問題
3. For higher accuracy, it is also advisable to calibrate the position of the screen as described by [Takahashiet al.](https://doi.org/10.2197/ipsjtcva.8.11), which provide an [OpenCV and matlab implementation](https://github.com/computer-vision/takahashi2012cvpr).
4. `python main.py --base_path=./data/p00`  ubuntu24.04版本後面參數還是要下完整
   1. This was only tested on Ubuntu 20.10 and Ubuntu 21.04. If you are using macOS or Windows, you might have to supply the monitor parameters manually, e.g., `--monitor_mm=750,420 --monitor_pixels=1920,1080`, and adjust the `TargetOrientation` values in `utils.py`.
5. Look at the screen and press the corresponding arrow key where the letter `E` is pointing at when the letter color changes from blue to orange. Please press the arrow key several times because sometimes OpenCV doesn't register the click the first time.
6. Press the `q` key when the data collection is complete.

![data collection example](./docs/demo.gif)

7. Visualize the recorded data, image by image by running `python visualization.py --base_path=./data/p00`.
(畫出資聊夾內的可視化圖片)

![visualization example](./docs/3d_plot.gif)
