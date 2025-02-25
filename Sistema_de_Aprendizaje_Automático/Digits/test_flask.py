import base64
from flask import Flask, request, jsonify
from PIL import Image
import cv2
import numpy as np
import tensorflow as tf
import io
from flask_cors import CORS

try:
    model = tf.keras.models.load_model('mnist_model.keras')
except Exception as e:
    print(f"Error al cargar el modelo: {e}")
    exit()

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        print("Request received")
        data = request.get_json()
        image_data = data['image']
        
        # Decodify the image and convert to grayscale
        img_data = base64.b64decode(image_data)
        img = Image.open(io.BytesIO(img_data)).convert('L')
       
        # Resize to 28x28 pixels and normalize
        img = img.resize((28, 28))
        # pass the image to an array
        img_array = np.array(img) / 255.0
        # ckeck the image in the backend for debugging, save the image kinda stop the server
        # img.save('uploaded_image.png')

        # In case that the canvas from the backend is white we have to pass it to black since the model
        # was trained with black background
        # img_array = 1 - img_array

        # Reshape previous array to a 4D array,
        # the first dimension is the batch size (1 in this case),
        # the second and third are the dimensions of the image (28x28),
        # and the last dimension is the number of channels (1 in this case)
        img_array = img_array.reshape(1, 28, 28, 1)  

        prediction = model.predict(img_array)
        digit = np.argmax(prediction)

        print({'prediction': str(digit)})
        return jsonify({'prediction': str(digit)})
    
    except Exception as e:
        return jsonify({'error': str(e)})


# copy and paste from class example
@app.route("/classify", methods=["POST"])
def classify_image():
    file = request.files["image"]
    if not file:
        return jsonify({"error": "No se proporcionó una imagen"}), 400

    # read and process the image
    image = np.asarray(bytearray(file.read()), dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (28, 28))  # reshape to a 28x28 image
    image = image / 255.0  # Normalize
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    image = np.expand_dims(image, axis=-1)  # Add color channel

    # realice prediction
    predictions = model.predict(image)
    label = np.argmax(predictions)

    return jsonify({"label": int(label)})


if __name__ == '__main__':
    app.run(debug=True)
