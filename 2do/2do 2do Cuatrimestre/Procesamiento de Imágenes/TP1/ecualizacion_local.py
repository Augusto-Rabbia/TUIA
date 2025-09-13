import cv2
import numpy as np
from math import ceil 
import matplotlib.pyplot as plt

def imshow(img, new_fig=True, title=None, color_img=False, blocking=False, colorbar=True, ticks=False):
    if new_fig:
        plt.figure()
    if color_img:
        plt.imshow(img)
    else:
        plt.imshow(img, cmap='gray')
    plt.title(title)
    if not ticks:
        plt.xticks([]), plt.yticks([])
    if colorbar:
        plt.colorbar()
    if new_fig:        
        plt.show(block=blocking)

img = cv2.imread('Imagen_con_detalles_escondidos.tif',cv2.IMREAD_GRAYSCALE)

def ecualizacion_local(img, ventana_proc: (int,int)):
    resultimg = img.copy()
    bordeY = ceil(ventana_proc[0]/2)
    bordeX = ceil(ventana_proc[1]/2)
    img_bord = cv2.copyMakeBorder(img, bordeY,bordeY,bordeX,bordeX, borderType= cv2.BORDER_REPLICATE)  
    
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            subimg = img_bord[y:y+ventana_proc[0],x:x+ventana_proc[1]]
            newSubimg = cv2.equalizeHist(subimg)
            resultimg[y][x] = newSubimg[bordeY][bordeX]
    imshow(resultimg)

ecualizacion_local(img, (5,5))
