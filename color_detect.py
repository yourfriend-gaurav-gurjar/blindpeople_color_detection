import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reading the image from the current folder
image = cv2.imread("pic.jpg")
cv2.imshow("Normal", image)


red_lower_color = np.array([136, 87, 111], np.uint8)
red_upper_color = np.array([180,255,255], np.uint8)
pink_lower_color = np.array([130, 0, 220], np.uint8)
pink_upper_color = np.array([170, 255, 255], np.uint8)
green_lower_color = np.array([38, 138, 40], np.uint8)
green_upper_color = np.array([70, 255, 255], np.uint8)

# Convert BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
red_mask = cv2.inRange(hsv, red_lower_color, red_upper_color)
pink_mask = cv2.inRange(hsv, pink_lower_color, pink_upper_color)
green_mask = cv2.inRange(hsv, green_lower_color, green_upper_color)

mask= red_mask + pink_mask + green_mask

cv2.imshow('mask', mask)
res = cv2.bitwise_and(image, image, mask=mask)

# Blue color's lower and upper values
blue_lower_color = np.array([100,128,0], np.uint8)
blue_upper_color = np.array([215, 255, 255], np.uint8)
#blue = cv2.cvtColor(res, [255,0,0], [0,255,0],[0,0,255])
#pink2Gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
# Convert Red color to Blue color
image[mask>0]=(255,0,0)
image[mask]
cv2.imwrite("result.jpg", image)
cv2.imwrite("red_result.jpg", image)

red_result = cv2.imread("red_result.jpg")
cv2.imshow("Blue", red_result)

#cv2.imshow('Blue', blue)





###
#image = np.zeros((400,400,3), dtype="uint8")
#raw = image.copy()
#image[np.where((image==[252,26,32]).all(axis=2))] = [144,129,54] # Red seen by protan
#image[np.where((image==[38,138,40]).all(axis=2))] = [148,113,50] # Green seen by  [turns into Brown]
#image[np.where((image==[138,45,224]).all(axis=2))] = [87,103,211] # Purple seen by protan (turns into Blue)
#image[np.where((image==[254,108,180]).all(axis=2))] = [170,156,172] # Pink seen by protan [turns into Gray]
#cv2.imshow('Test', image)
cv2.imshow('Test2', res)
if cv2.waitKey() == ord('q'):
    cv2.destroyAllWindows()


###

#cv2.imshow('res', res)
#cv2.imshow('pink_res', pink_res)



#cv2.waitKey(0)
#image[np.where((image==[]))]


# Convert Pink color to Gray color
#image[mask>0]=(255,0,0)
#cv2.imwrite("result.jpg", image)
#result = cv2.imread("result.jpg")
#cv2.imshow("Gray", result)

#cv2.waitKey(0)

#cv2.destroyAllWindows()
