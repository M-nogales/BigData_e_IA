# Proyecto: Reconocimiento de Matrículas en Imágenes con IA

## Descripción del Proyecto

Desarrollar una aplicación web que permita a los usuarios cargar imágenes en formato JPEG o PNG y extraiga automáticamente la matrícula del vehículo presente en la imagen.

### Tecnologías a Utilizar

- **Backend**: Flask
- **OCR**: Tesseract
- **Preprocesamiento de imágenes**: OpenCV
- **Frontend**: HTML, JavaScript

## Requisitos del Proyecto

1. **Backend (Servidor Flask)**:
   - Crear un servidor Flask que procese las imágenes cargadas y devuelva la matrícula detectada en formato JSON.
   - Si no se puede identificar la matrícula, el servidor debe devolver un mensaje de error.

2. **Modelo de Reconocimiento de Matrículas**:
   - Implementar un modelo OCR utilizando **Tesseract** en Python para detectar las matrículas en las imágenes.
   - Utilizar **OpenCV** para el preprocesamiento de las imágenes (ajustar resolución, eliminar ruido, etc.).

3. **Frontend**:
   - Crear una interfaz HTML con un botón para permitir que los usuarios suban imágenes.
   - Mostrar un área donde se visualizará el resultado con la matrícula detectada.
   
4. **Consola**:
   - Al finalizar la ejecución, imprimir en la consola un listado con todas las matrículas identificadas.

## Flujo de Trabajo

1. El usuario sube una imagen (JPEG o PNG).
2. El backend recibe la imagen y la procesa utilizando Tesseract para detectar la matrícula.
3. El servidor Flask devuelve la matrícula detectada o un mensaje de error en formato JSON.
4. El frontend muestra el resultado (matrícula o mensaje de error) al usuario.
5. Se imprime un listado de todas las matrículas identificadas en la consola.

## Requisitos Técnicos

- **Python**: Lenguaje de programación.
- **Flask**: Framework web para el backend.
- **Tesseract**: Herramienta de OCR para el reconocimiento de texto.
- **OpenCV**: Biblioteca para el procesamiento de imágenes.
- **HTML y JavaScript**: Para el desarrollo del frontend.

## Ajustes

En mi caso he usado **easyocr** en vez de **Tesseract** por posibles problemas de permisos en la instalación de **Tesseract**