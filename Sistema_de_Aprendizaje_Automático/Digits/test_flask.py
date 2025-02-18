from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
import tensorflow as tf
import io
import base64
from flask_cors import CORS

# Cargar el modelo entrenado (sustituye 'model_path' con la ubicación de tu modelo)
try:
    model = tf.keras.models.load_model('model_path')
except Exception as e:
    print(f"Error al cargar el modelo: {e}")
    exit()

# Crear la aplicación Flask
app = Flask(__name__)
CORS(app)  # Habilitar CORS si es necesario para solicitudes desde otros dominios

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        image_data = data['image']
        
        # Decodificar la imagen base64
        img_data = base64.b64decode(image_data.split(',')[1])
        img = Image.open(io.BytesIO(img_data)).convert('L')
        
        # Redimensionar la imagen a 28x28 y normalizar
        img = img.resize((28, 28))
        img_array = np.array(img) / 255.0
        
        # Predecir el dígito
        img_array = img_array.reshape(1, 28, 28, 1)
        prediction = model.predict(img_array)
        digit = np.argmax(prediction)
        
        return jsonify({'prediction': str(digit)})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

# py -3.12 c:/Users/alumno/Desktop/Tarde_BigData/BigData_e_IA/Sistema_de_Aprendizaje_Automático/Digits/test_flask.py