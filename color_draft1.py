import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("pic.jpg")
image_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#cv2.imshow(image_RGB)
plt.figure(figsize=(20,8))
plt.imshow(image_RGB)
