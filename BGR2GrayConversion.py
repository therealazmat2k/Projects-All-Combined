import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('E:\Sugarcane\pictures\\newimage.jpg')



gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#kernel = np.ones((3,3),np.uint8)


kernel = np.array([[1, 0, 0],
                   [1, 0, 0],
                   [1, 0, 0]], np.uint8)

gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('gradient', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
