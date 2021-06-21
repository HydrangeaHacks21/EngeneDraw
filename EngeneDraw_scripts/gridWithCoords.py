import os
import cv2
import numpy as np

image = cv2.imread('images/piplup.png')

width, height, channels = image.shape

while (width > 800 or height > 600):
    scale_percent = 80  # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    image = resized

num_squares_row = 10
line_thickness = 2

dist = width / num_squares_row
num_squares_col = int(height / dist)

for i in range(1, num_squares_row):
    x1, y1 = dist * i, 0
    x2, y2 = dist * i, height

    cv2.line(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), thickness=line_thickness)

for j in range(1, num_squares_col):
    x1, y1 = 0, dist * j
    x2, y2 = width, dist * j

    cv2.line(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), thickness=line_thickness)

cv2.imshow('grids', image)

cv2.waitKey(0)




