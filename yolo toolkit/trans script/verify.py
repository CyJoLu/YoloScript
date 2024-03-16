import numpy as np
import cv2

# 读取标签
label_path = r"E:\Edge Downloads\labelme2yolo-main\labelme2yolo-main\YOLODataset\val\labels\B-0020_BMGZGY22_527564.txt"
# 读取图像
img = cv2.imread(r"E:\Edge Downloads\labelme2yolo-main\labelme2yolo-main\YOLODataset\val\images\B-0020_BMGZGY22_527564.jpg")

height, width, channels = img.shape

with open(label_path,'r') as f:
    current_line = f.readline()
    while current_line:
        temp_list = current_line.split(' ')
        x = int(float(temp_list[1])*width)
        y = int(float(temp_list[2])*height)
        w = int(float(temp_list[3])*width)
        h = int(float(temp_list[4])*height)

        x1 = int(x-w/2)
        y1 = int(y-h/2)
        x2 = int(x+w/2)
        y2 = int(y+h/2)
        cv2.rectangle(img, (x1, y1), (x2,y2), (0, 0, 255), 2 )
        current_line = f.readline()

winname = 'showImg'
cv2.namedWindow(winname)
cv2.imshow(winname, img)
cv2.waitKey(0)
cv2.destroyWindow(winname)
# 保存图像
cv2.imwrite('test.jpg',img)

