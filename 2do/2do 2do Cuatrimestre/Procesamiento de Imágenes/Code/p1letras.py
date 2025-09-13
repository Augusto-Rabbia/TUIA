import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("letras.png", cv.IMREAD_GRAYSCALE)

plt.imshow(img, cmap="gray")
plt.show(block=False)                    



