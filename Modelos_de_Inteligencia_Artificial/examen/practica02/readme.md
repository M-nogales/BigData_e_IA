# Chatbot con Reglas y Respuestas Basadas en Similaridad
crear un chatbot básico que pueda responder preguntas utilizando reglas predefinidas y análisis de similitud de texto.

    1. Utiliza Python con las librerías nltk y sklearn.feature_extraction.text.TfidVectorizer.
    2. Define un conjunto de preguntas y respuestas predefinidas (mínimo 10 pares de pregunra-respuesta)
    3. implementa una lógica que compare la pregunta del usuario con las preguntas almacenadas usando similitud del coseno
    4. si la similitudes alta (ej. mayor que el 75%),el chatbotdevuelve la respuesta más cercana.
    5. si la similitud es baja, el chatbot responde con "No entiendo tu pregunta intenta reformularla"
    6. permitir que el usuario haga múltiples preguntas hasta que escriba "salir"
    7. Documentar el código con comentarios y generar un informe con ejemplos de interacción  