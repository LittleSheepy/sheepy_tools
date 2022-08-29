import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("111.jpg", cv2.IMREAD_GRAYSCALE)
template = cv2.imread("template.jpg", cv2.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where(res >= 0.9)
for i in zip(*loc[::-1]):
    cv2.rectangle(img, i, (i[0] + w, i[1] + h), (255, 0, 255), 2)
plt.imshow(img, cmap='gray')
plt.axis("off")
plt.show()