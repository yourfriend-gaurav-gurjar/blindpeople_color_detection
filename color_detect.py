import cv2
import numpy as np

# Reading the image from the current folder
image = cv2.imread("pic.jpg")
cv2.imshow("Normal", image)

# Red Color's lower and upper values
red_lower_color = np.array([136, 87, 111], np.uint8)
red_upper_color = np.array([180,255,255], np.uint8)

# Convert BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, red_lower_color, red_upper_color)
cv2.imshow('mask', mask)

# Red Color detected
res = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow('res', res)

# Blue color's lower and upper values
blue_lower_color = np.array([100,128,0], np.uint8)
blue_upper_color = np.array([215, 255, 255], np.uint8)


# Convert Red color to Blue color
image[mask>0]=(255,0,0)
cv2.imwrite("result.jpg", image)
result = cv2.imread("result.jpg")
cv2.imshow("Blue", result)

cv2.waitKey(0)

cv2.destroyAllWindows()
