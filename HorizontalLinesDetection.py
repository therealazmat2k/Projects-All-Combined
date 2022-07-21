import cv2
import numpy as np

img = cv2.imread('E:\Sugarcane\pictures\Gradient.png')

mask = img[:, :, 0]

height, width = mask.shape

mask = cv2.threshold(mask, 100, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("mask", mask)

vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, height // 30))
vertical_lines = cv2.erode(mask, vertical_kernel, iterations=1)
vertical_lines = cv2.dilate(vertical_lines, vertical_kernel, iterations=1)

# cv2.imshow("vertical_lines", vertical_lines)

img[vertical_lines > 0, 2] = 255
cv2.imshow("final", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

