import cv2

# 打開攝像頭
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

            # 嘗試設置幀率
fps = 30
cap.set(cv2.CAP_PROP_FPS, fps)

            # 獲取實際設置的幀率
actual_fps = cap.get(cv2.CAP_PROP_FPS)

if int(actual_fps) == fps:
   print(f"FPS {fps} is supported")
else:
   print(f"FPS {fps} is not supported")
   print(f"Actual FPS: {actual_fps}")

cap.release()

