import cv2

# 测试图片路径
image_path = "../Flock_of_sheep.jpg"  # 确保这里替换为你实际的图片路径

# 尝试加载图片
image = cv2.imread(image_path)

if image is None:
     print(f"无法加载图片，请检查路径是否正确: {image_path}")
else:
     print("图片加载成功！显示图片窗口...")

                # 显示图片
     cv2.imshow("OpenCV Image Test", image)

                        # 等待按键
    

          # 等待按键（如按下 ESC 键或任意键退出）
     print("按 'q' 键退出...")
     while True:
         key = cv2.waitKey(1) & 0xFF  # 读取键盘输入
         if key == ord('q'):  # 按下 'q' 键退出
             print("退出窗口...")
             break
     cv2.destroyAllWindows()
