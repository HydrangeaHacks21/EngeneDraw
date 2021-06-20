import os

import cv2
import numpy as np
import PIL

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

# img_1 = np.zeros([width, height, 3], dtype=np.uint8)
#
# img_1.fill(255)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



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

print(mapped_array)

mapped_array = mapped_array.astype(np.uint8)

cv2.imshow('All Contours', mapped_array)

path = 'C:/Users/Amelia/Documents/GitHub/pythonTesting/images'

cv2.imwrite(os.path.join(path, 'pipGray.jpg'), mapped_array)

# cv2.waitKey(0)
