import os

import cv2
import numpy as np

image= cv2.imread('cartoons/babyShark.png')

width, height, b = image.shape

img_1 = np.zeros([width,height,1],dtype=np.uint8)

img_1.fill(255)

gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges= cv2.Canny(gray,30,200)

contours, hierarchy= cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

#cv2.imshow('All Contours', img_1)

print(type(img_1))

length = len(contours)

path = 'C:/Users/Amelia/Documents/GitHub/pythonTesting/colder'
sum_pixels = 0

for i in range(0, length):
    sum_pixels += len(contours[length - i - 1])
    cv2.drawContours(img_1, contours, (length - i - 1), (0, 255, 0), 1)

    if (sum_pixels >= 20):
        cv2.imwrite(os.path.join(path, '{}.jpg'.format(i)), img_1)
        sum_pixels = 0

cv2.imwrite(os.path.join(path, '{}.jpg'.format(length)), img_1)

cv2.waitKey(0)
