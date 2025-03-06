import cv2
import numpy as np
from flask import Flask, request, jsonify, render_template, send_file, Response
import easyocr
import imutils
from io import BytesIO
import base64

app = Flask(__name__)

# Ruta para la página principal que permite subir imágenes
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para procesar la imagen subida
@app.route('/upload', methods=['POST'])
def upload():
    if 'license-image' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['license-image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    # Leer la imagen directamente desde la memoria
    file_bytes = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    
    # Procesar la imagen y obtener la matrícula recortada
    cropped_image, text = process_image(img)
    
    if cropped_image is None:
        return jsonify({'error': 'No se pudo detectar la matrícula'})
    
    # Convertir la imagen recortada en bytes
    _, buffer = cv2.imencode('.jpg', cropped_image)
    img_bytes = BytesIO(buffer)
    
    # Regresar los datos: imagen en base64 y texto reconocido
    img_base64 = base64.b64encode(img_bytes.getvalue()).decode('utf-8')
    
    return jsonify({
        'image': img_base64,
        'text': text
    })

def process_image(img):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bfilter = cv2.bilateralFilter(gray_image, 5, 15, 15)
    edged = cv2.Canny(bfilter, 50, 150)

    keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(keypoints)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    location = None
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 10, True)
        if len(approx) == 4:
            location = approx
            break
    
    if location is None:
        return None, "Matrícula no detectada"
    
    mask = np.zeros(gray_image.shape, np.uint8)
    cv2.drawContours(mask, [location], 0, 255, -1)
    new_image = cv2.bitwise_and(img, img, mask=mask)
    
    (x, y) = np.where(mask == 255)
    (x1, y1) = (np.min(x), np.min(y))
    (x2, y2) = (np.max(x), np.max(y))
    cropped_image = img[x1:x2+1, y1:y2+1]
    
    reader = easyocr.Reader(['en'])
    result = reader.readtext(cropped_image)
    text = result[0][-2] if result else "Matrícula no detectada"
    
    return cropped_image, text

if __name__ == '__main__':
    app.run(debug=True)
