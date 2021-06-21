import os
import sys
import cv2
import numpy as np

image = cv2.imread(sys.argv[1])

gridSize = int(sys.argv[2])
thickness = int(sys.argv[3])

height, width, b = image.shape

print(width, height)

img_1 = np.zeros([height,width,1],dtype=np.uint8)

img_1.fill(255)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray,150,200)

contours, hierarchy= cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

w = round(width / gridSize)
h = round(height / gridSize)

w_cont = w
h_cont = h

#add vertical lines
for i in range (0, gridSize - 1):

    cv2.line(img_1,(w_cont,0),(w_cont,height),(0,255,0),thickness)
    w_cont += w

for j in range (0, gridSize - 1):

    cv2.line(img_1, (0,h_cont),(width,h_cont),(0,255,0),thickness)
    h_cont += h

cv2.imwrite('test.jpg', img_1)

print(type(img_1))

length = len(contours)

for i in range(0, length):
    cv2.drawContours(img_1, contours, i, (0, 255, 0), 3)
    cv2.imwrite('{}.jpg'.format(i), img_1)


