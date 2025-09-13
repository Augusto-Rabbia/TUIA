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

def encontrar_lineas(img):
    binary_img = img < 128
    verticales = []
    horizontales = []
    for row in range(img.shape[0]):
        es_linea = np.sum(binary_img[row,:]) > 400
        if es_linea:
            horizontales.append(row)
    for col in range(img.shape[1]):
        es_linea = np.sum(binary_img[:,col]) > 300
        if es_linea:
            verticales.append(col)
    return (verticales, horizontales)

def contar_caracteres_y_palabras(campo):
    palabras = 1
    num_etiqs, etiqs, stats, centroides = cv2.connectedComponentsWithStats(campo, 8, cv2.CV_32S)
    extremos_derecha = []
    extremos_izquierda = []

    for i in range(1,num_etiqs-1):
        extremos_izquierda.append(stats[i+1][0])
        extremos_derecha.append(stats[i][0]+stats[i][2])

    extremos_izquierda.sort()
    extremos_derecha.sort()

    for i in range(num_etiqs-2):
        if (extremos_izquierda[i] - extremos_derecha[i]) > 6:
            palabras +=1

    return palabras, num_etiqs-1+palabras-1

def chequear_validez(campo, letrasMAX = None, palabrasMAX = None, letrasMIN = None, palabrasMIN = None):
    palabras, caracteres = contar_caracteres_y_palabras(campo)
    if letrasMAX != None and caracteres > letrasMAX: 
        return False
    if palabrasMAX != None and palabras > palabrasMAX:
        return False
    if letrasMIN != None and letrasMIN > caracteres: 
        return False
    if palabrasMIN != None and palabrasMIN > palabras:
        return False
    return True

def main():
    form = input("Ingrese el path hacia la imagen del formulario: ")
    img = cv2.imread(form,cv2.IMREAD_GRAYSCALE)
    binary_img = img.copy()
    binary_img[img>160] = 0
    binary_img[img<=160] = 255

    # Obtenemos todas las lineas
    verticales, horizontales = encontrar_lineas(img)

    campo_titulo = binary_img[(horizontales[0]+3):(horizontales[1]-3),(verticales[0]+3):(verticales[2]-3)]

    campo_nom_ape = binary_img[(horizontales[1]+3):(horizontales[2]-2),(verticales[1]+3):(verticales[2]-3)]

    campo_edad = binary_img[(horizontales[2]+3):(horizontales[3]-3),(verticales[1]+3):(verticales[2]-3)]

    campo_mail = binary_img[(horizontales[3]+3):(horizontales[4]-3),(verticales[1]+3):verticales[2]-3]

    campo_legajo = binary_img[(horizontales[4]+3):(horizontales[5]-3),(verticales[1]+3):verticales[2]-3]

    campo_si_no = binary_img[(horizontales[5]+3):(horizontales[6]-3),(verticales[1]+3):verticales[2]-3]

    campo_comentarios = binary_img[(horizontales[-3]+3):(horizontales[-2]-3),(verticales[1]+3):verticales[2]-3]
    pregunta1 = binary_img[(horizontales[6]+1):(horizontales[7]-1),(verticales[1]+1):verticales[-1]]
    pregunta2 = binary_img[(horizontales[7]+1):(horizontales[8]-1),(verticales[1]+1):verticales[-1]]
    pregunta3 = binary_img[(horizontales[8]+1):(horizontales[9]-1),(verticales[1]+1):verticales[-1]]

    vale_nom_ape = chequear_validez(campo_nom_ape, letrasMAX=25, palabrasMIN=2)
    # Decidimos no aceptar espacios para este campo
    vale_edad = chequear_validez(campo_edad, letrasMAX=3, letrasMIN=2, palabrasMAX=1)
    vale_mail = chequear_validez(campo_mail, palabrasMAX=1, letrasMAX=25)
    vale_legajo = chequear_validez(campo_legajo, palabrasMIN=1, palabrasMAX=1, letrasMAX=8, letrasMIN=8)
    vale_comentarios = chequear_validez(campo_comentarios, letrasMAX=25)
    # Buscamos 3 porque nuestro algoritmo contará la línea media como un separador entre 2 letras.
    vale_preg1 = chequear_validez(pregunta1, letrasMAX=1+1, letrasMIN=1+1)
    vale_preg2 = chequear_validez(pregunta2, letrasMAX=1+1, letrasMIN=1+1)
    vale_preg3 = chequear_validez(pregunta3, letrasMAX=1+1, letrasMIN=1+1)
    campos = ["Nombre y Apellido", "Edad", "Mail", "Legajo", "Pregunta 1", "Pregunta 2", "Pregunta 3", "Comentarios"]
    resultados = [vale_nom_ape, vale_edad, vale_mail, vale_legajo, vale_preg1, vale_preg2, vale_preg3, vale_comentarios]
    for i in range(len(campos)):
        if resultados[i]: res = "OK"
        else: res = "MAL"
        print(f"{campos[i]:20}:{res}")

main()
