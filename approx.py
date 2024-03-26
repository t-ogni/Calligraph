 
import cv2
import numpy as np

# Загрузка изображения буквы "А"
image = cv2.imread('abc.png', cv2.IMREAD_GRAYSCALE)

# Очистка изображения от шумов и случайных небольших линий
kernel = np.ones((1, 1), np.uint8)
cleaned_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# Применение пороговой обработки
_,binary_image = cv2.threshold(cleaned_image,220,255,cv2.THRESH_BINARY_INV)

# Нахождение контуров буквы
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Аппроксимация контура буквы с помощью линий
lines = []
for contour in contours:
    epsilon = 0.01 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    for i in range(len(approx) - 1):
        start_point = tuple(approx[i][0])
        end_point = tuple(approx[i + 1][0])
        lines.append([start_point, end_point])

# Вывод набора движений
print(lines)

from turtle import Turtle

t = Turtle()
t.speed(0)
t.screen.screensize(5000,5000)
# for j in lines:
# 	t.pu()
# 	t.setpos(j[0][0], -j[0][1])
# 	t.pd()
# 	t.setpos(j[1][0], -j[1][1])

t.pu()	
t.setpos(100,100)

res = []
for x in contours:
	letter = []
	for i in x:
		letter.append(list(i[0]))
	res.append(letter)
with open('letters.py', 'w') as f:
	f.write('dict = '+str(res))

for c in contours:
	t.pu()
	for a in c:
		for i in a:
			t.setpos(i[0], -i[1]+300)
			t.pd()

t.screen.mainloop()
