import cv2
import numpy as np

def find_skeleton3(img):
    skeleton = np.zeros(img.shape,np.uint8)
    eroded = np.zeros(img.shape,np.uint8)
    temp = np.zeros(img.shape,np.uint8)

    _,thresh = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)

    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))

    iters = 0
    while(True):
        cv2.erode(thresh, kernel, eroded)
        cv2.dilate(eroded, kernel, temp)
        cv2.subtract(thresh, temp, temp)
        cv2.bitwise_or(skeleton, temp, skeleton)
        thresh, eroded = eroded, thresh # Swap instead of copy

        iters += 1
        if cv2.countNonZero(thresh) == 0:
            return (skeleton,iters)

# Загрузка изображения
img = cv2.imread('abc.png', cv2.IMREAD_GRAYSCALE)
cv2.normalize(img, img, 0, 255, cv2.NORM_MINMAX)

# Очистка изображения от шумов и случайных небольших линий
kernel = np.ones((1, 1), np.uint8)
cleaned_image = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# Скелетонизация изображения
skel, t = find_skeleton3(cleaned_image)

# Отображение скелетонизированного изображения
cv2.imshow(f'[{t}] Skeletonized Image', skel)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Перевод скелета в линии
skeleton_points = np.argwhere(skel > 0)
lines = []


for point in skeleton_points:
    x, y = point[1], point[0]
    neighbors = skel[y-1:y+2, x-1:x+2]
    if np.sum(neighbors) <= 255:
        start_point = (x, y)
        end_point = tuple(point)
        lines.append([start_point, end_point])


from turtle import Turtle

t = Turtle()
t.speed(0)
t.screen.screensize(5000,5000)
for j in lines:
	t.pu()
	t.setpos(j[0])
	t.pd()
	t.setpos(j[1])

t.screen.mainloop()
