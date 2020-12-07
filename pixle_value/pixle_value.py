
import numpy as np
import cv2

image = cv2.imread('water_coins.jpg')

image_width_index =np.shape([[1,2]])
image_height_index = np.shape([0])

print(image[0, 0])
print(image[image_height_index, image_height_index])
h, w, ch_numbers = np.shape(image)

for py in range(0,h):
    for px in range(0,w):
        print('Pixel value of Pos {}:{} is {}'.format(py, px, image[py][px]))
