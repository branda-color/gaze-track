import cv2

cap = cv2.VideoCapture(0)  # 嘗試打開攝像頭
if not cap.isOpened():
    print("Cannot open camera")
    exit()
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))
while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame. Exiting ...")
        break
    out.write(frame)
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):  # 按 Q 結束
        print("out of window")
        break

cap.release()
out.release()
cv2.destroyAllWindows()

