import os
import cv2
import numpy as np
from flask import Flask, request, jsonify, render_template
import easyocr
import imutils

app = Flask(__name__)

# Ruta para la página principal que permite subir imágenes
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para procesar la imagen subida
@app.route('/upload', methods=['POST'])
def upload():
    # Verificar si la solicitud tiene un archivo
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    
    # Si no se seleccionó un archivo
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Guardar el archivo temporalmente
    img_path = os.path.join('uploads', file.filename)
    file.save(img_path)

    # Llamar a la función para extraer la matrícula
    text = process_image(img_path)
    
    # Devolver el número de matrícula extraído
    return jsonify({'matricula': text})

# Función para procesar la imagen y extraer el texto de la matrícula
def process_image(img_path):
    # Leer la imagen y convertirla a escala de grises
    img = cv2.imread(img_path)
    h, w = img.shape[:2]

    normalized_img = cv2.normalize(img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    gray_image = cv2.cvtColor(normalized_img, cv2.COLOR_BGR2GRAY)

    # Aplicar filtro y encontrar bordes
    bfilter = cv2.bilateralFilter(gray_image, 5, 15, 15)
    edged = cv2.Canny(bfilter, 50, 150)

    # Encontrar contornos
    keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(keypoints)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    # Localizar la matrícula
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 10, True)
        if len(approx) == 4:
            location = approx
            break

    # Crear una máscara para la matrícula
    mask = np.zeros(gray_image.shape, np.uint8)
    new_image = cv2.drawContours(mask, [location], 0, 255, -1)
    new_image = cv2.bitwise_and(img, img, mask=mask)

    # Recortar la imagen de la matrícula
    (x, y) = np.where(mask == 255)
    (x1, y1) = (np.min(x), np.min(y))
    (x2, y2) = (np.max(x), np.max(y))
    cropped_image = gray_image[x1:x2+1, y1:y2+1]

    # Leer el texto usando easyocr
    reader = easyocr.Reader(['en'])
    result = reader.readtext(cropped_image)
    
    # Extraer el texto de la matrícula
    if result:
        return result[0][-2]
    else:
        return 'Matrícula no detectada'

if __name__ == '__main__':
    app.run(debug=True)
