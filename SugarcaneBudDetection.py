# import libraries
import cv2
import numpy as np


# 1st function to convert Original image to gray
def bgr2gray():
    image = cv2.imread('E:\Sugarcane\pictures\img1.jpeg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Original image', image)
    cv2.imshow('Gray image', gray)
    cv2.waitKey(0)


# 2nd Fun to gray to gradient image with input gray
def gradient():
    gray = cv2.imread('E:\Sugarcane\pictures\gray.png')
    kernel = np.ones((5, 5), np.uint8)
    grad = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow("Gradient", grad)
    cv2.waitKey(0)


# 3rd function for final operations with input grad
def finaloperations():
    grad = cv2.imread('E:\Sugarcane\pictures\Gradient.png')
    mask = grad[:, :, 0]
    height, width = mask.shape
    mask = cv2.threshold(mask, 100, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow("mask", mask)
    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, height // 30))
    vertical_lines = cv2.erode(mask, vertical_kernel, iterations=1)
    vertical_lines = cv2.dilate(vertical_lines, vertical_kernel, iterations=1)
    grad[vertical_lines > 0, 2] = 255
    cv2.imshow("final", grad)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


print("", bgr2gray())
print("", gradient())
print("", finaloperations())

