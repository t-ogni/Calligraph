import numpy as np

import cv2

img = cv2.imread('caligr.png', cv2.IMREAD_GRAYSCALE)

(thresh, im_bw) = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY )
cv2.imwrite('bw_image.png', im_bw)
img = im_bw
result_fill = np.ones(img.shape, np.uint8) * 255
result_borders = np.zeros(img.shape, np.uint8)

# the '[:-1]' is used to skip the contour at the outer border of the image
contours = cv2.findContours(img, cv2.RETR_LIST,
                            cv2.CHAIN_APPROX_SIMPLE)[0][:-1]

from turtle import Turtle
from random import random

t = Turtle()
t.screen.screensize(7000,7000)
for j in contours:
	t.pu()
	for i in j:
		t.setpos(i[0][0], -i[0][1])
		t.pd()

# t.screen.mainloop()

print(len(contours[0]))
# fill spaces between contours by setting thickness to -1
cv2.drawContours(result_fill, contours, -1, 0, -1)
cv2.drawContours(result_borders, contours, -1, 255, 1)

# xor the filled result and the borders to recreate the original image
result = result_fill ^ result_borders

# prints True: the result is now exactly the same as the original
print(np.array_equal(result, img))

cv2.imwrite('contours.png', result)
