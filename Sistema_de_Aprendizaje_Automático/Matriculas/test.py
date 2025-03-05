import easyocr
import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils

#1. Leer la imagen y convertirla a escala de grises
img = cv2.imread('imgs_test/Cars16.png')
h, w = img.shape[:2]
plt.imshow(img)
plt.show()
normalized_img = cv2.normalize(img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

gray_image = cv2.cvtColor(normalized_img, cv2.COLOR_BGR2GRAY)

plt.imshow(gray_image, cmap='gray')
plt.show()

#2. Aplicar filtro y encontrar bordes para localización
bfilter = cv2.bilateralFilter(gray_image, 5, 15, 15) #filtro para reducir ruido de una imagen y sin eliminar bordes
edged = cv2.Canny(bfilter, 50, 150) #Detección de bordes con algoritmo de detección de bordes Canny
plt.imshow(edged, cmap='gray')
plt.show()

#3. Encontrar contornos y aplicar máscara
# busca las areas cerradas, con el modo de jerarquía de contornos RETR_TREE
keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(keypoints)
# ordena los contornos por área de mayor a menor y toma los 10 primeros
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

for contour in contours:
    # Aproxima cada contorno a un polígono simplificado con menos vértices.
    #  la matrícula es un cuadrilátero (4 vértices)
    approx = cv2.approxPolyDP(contour, 10, True)
    if len(approx) == 4:
        location = approx
        break
print(location)

# crea una máscara en blanco y dibuja el contorno detectado
mask = np.zeros(gray_image.shape, np.uint8)
new_image = cv2.drawContours(mask, [location], 0,255, -1)
new_image = cv2.bitwise_and(img, img, mask=mask)
plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
plt.show()

# Buscamos las areas en las que la máscara tiene un valor de 255, es decir los bordes de la matrícula
# y recortamos la imagen original para quedarnos solo con la matrícula
(x,y) = np.where(mask==255)
(x1, y1) = (np.min(x), np.min(y))
(x2, y2) = (np.max(x), np.max(y))
cropped_image = gray_image[x1:x2+1, y1:y2+1]
plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
plt.show()
#4. Leer texto con easyocr
reader = easyocr.Reader(['en'])
result = reader.readtext(cropped_image)
result

#5. Imprimir los resultados
text = result[0][-2]
font = cv2.FONT_HERSHEY_SIMPLEX
# Colocar el texto justo debajo
offset_x = w * 0.05  # 10% del ancho de la imagen
offset_y = h * 0.23  # 20% del alto de la imagen

# Añadir el texto y el rectángulo en la imagen
res = cv2.putText(img, text=text, org=(location[0][0][0] - int(offset_x), location[1][0][1] + int(offset_y)),
                      fontFace=font, fontScale=1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
res = cv2.rectangle(img, tuple(approx[0][0]), tuple(approx[2][0]), (0,255,0),3)
plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
plt.show()
print(result)
