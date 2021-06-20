import os
import cv2
import numpy as np

image = cv2.imread('images/piplup.png')

width, height, b = image.shape

print(width)
while (width > 800 or height > 600):
    scale_percent = 80  # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    image = resized



gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

backtorgb = cv2.cvtColor(gray,cv2.COLOR_GRAY2RGB)

def simplify(x):
    if x <= 15:
        return 0
    elif 15 < x <= 51:
        return 15
    elif 51 < x <= 102:
        return 51
    elif 102 < x <= 153:
        return 102
    elif 153 < x <= 204:
        return 153
    elif 204 < x <= 51:
        return 204
    else:
        return 255

simplify_vectorized = np.vectorize(simplify)

mapped_array = simplify_vectorized(gray)

mapped_array = mapped_array.astype(np.uint8)

cv2.imshow('All Contours', mapped_array)

backtorgb = cv2.cvtColor(mapped_array, cv2.COLOR_GRAY2RGB)

cv2.waitKey(0)

cv2.imshow('All colors', backtorgb)

cv2.waitKey(0)

# path = 'C:/Users/Amelia/Documents/GitHub/pythonTesting/images'

# cv2.imwrite(os.path.join(path, 'pipGray.jpg'), mapped_array)

print(backtorgb[200][200][1])

backtorgb[np.where((backtorgb==[0,0,0]).all(axis=2))] = [90, 4, 0]
backtorgb[np.where((backtorgb==[15,15,15]).all(axis=2))] = [90, 3, 2]
backtorgb[np.where((backtorgb==[51,51,51]).all(axis=2))] = [120, 3, 23]
backtorgb[np.where((backtorgb==[102,102,102]).all(axis=2))] = [180, 50, 2]
backtorgb[np.where((backtorgb==[153,153,153]).all(axis=2))] = [200,33,22]
backtorgb[np.where((backtorgb==[204,204,204]).all(axis=2))] = [230, 136, 120]
backtorgb[np.where((backtorgb==[255,255,255]).all(axis=2))] = [242, 240, 172]


cv2.imshow('Final', backtorgb)

cv2.waitKey(0)
