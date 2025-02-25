# Aplicación Web de Reconocimiento de Dígitos

## Instalación y Configuración

1. Asegúrate de tener instalada la librería DIGITS.
2. Descarga o genera el dataset MNIST para entrenar un modelo de reconocimiento de dígitos.
3. Entrena un modelo de clasificación de imágenes usando DIGITS.

## Entrenamiento del Modelo

1. Importa el conjunto de datos MNIST en DIGITS.
2. Configura una red neuronal para clasificar los números del 0 al 9.
3. Entrena el modelo y expórtalo para su uso posterior.

## Desarrollo de la Interfaz Web

1. Crea una página web con HTML, CSS y JavaScript que incluya:
   - Un lienzo (`<canvas>`) donde el usuario pueda dibujar un número.
   - Un botón para enviar la imagen al modelo de predicción.
   - Un área donde se muestre el resultado.

## Integración con el Modelo de IA

1. Implementa un backend en Flask o FastAPI que reciba la imagen, la procese y la envíe al modelo entrenado.
2. Convierte la imagen del usuario en un formato compatible con el modelo (28x28 píxeles, escala de grises).
3. Ejecuta la predicción y devuelve el número identificado.

## Pruebas y Optimización

1. Realiza pruebas con distintos números escritos a mano.
2. Ajusta la precisión del modelo si es necesario.
3. Mejora la interfaz y la experiencia de usuario.

## Entrega

1. Fichero Python con el desarrollo del código y del algoritmo.
2. Documenta cada paso a través de comentarios de código.

live server to open html and fetch:
https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer

libraries:
# pip install flask pillow opencv-python numpy tensorflow flask-cors
