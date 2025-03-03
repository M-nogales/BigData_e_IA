from flask import Flask, request, jsonify
import pytesseract
import cv2
import numpy as np
from PIL import Image
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configura la ruta de Tesseract si es necesario (en Windows por ejemplo)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Ajusta esta ruta si es necesario

def process_image(image_path):
    # Cargar la imagen
    image = cv2.imread(image_path)
    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Aplicar un umbral para mejorar el contraste
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    # Usar Tesseract para obtener el texto
    text = pytesseract.image_to_string(thresh, config='--psm 8')
    return text.strip()

@app.route('/upload', methods=['POST'])
def upload_image():
    # Verifica si el archivo está presente en la solicitud
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Guarda la imagen en un directorio temporal
    image_path = os.path.join("uploads", file.filename)
    file.save(image_path)

    # Procesar la imagen y extraer la matrícula
    license_plate = process_image(image_path)

    if license_plate:
        print(f"Matrícula identificada: {license_plate}")
        return jsonify({"license_plate": license_plate})
    else:
        return jsonify({"error": "No se pudo identificar la matrícula"}), 400

if __name__ == '__main__':
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
    app.run(debug=True)
