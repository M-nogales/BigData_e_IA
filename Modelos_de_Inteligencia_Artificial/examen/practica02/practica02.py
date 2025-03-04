import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

# Descargar recursos necesarios de NLTK
nltk.download('punkt')
nltk.download('stopwords')

# Configurar el stemmer y las stopwords para español
stemmer = SnowballStemmer('spanish')
stop_words = set(stopwords.words('spanish'))

def preprocess_text(text):
    # Preprocesa el texto eliminando stopwords y aplicando stemming.

    tokens = nltk.word_tokenize(text.lower())
    filtered_tokens = [stemmer.stem(word) for word in tokens if word.isalnum() and word not in stop_words]
    return " ".join(filtered_tokens)

# Definir el conjunto de preguntas y respuestas predefinidas
qa_pairs = {
    "¿Cómo te llamas?": "Soy un chatbot de prueba.",
    "¿Qué puedes hacer?": "Puedo responder preguntas basadas en similitud de texto.",
    "¿Cómo funciona este chatbot?": "Utilizo la similitud del coseno para encontrar la mejor respuesta a tu pregunta.",
    "¿Quién te creó?": "Fui creado por un desarrollador con Python (extremadamente guapo) y bibliotecas de procesamiento de lenguaje natural.",
    "¿Cuál es la capital de Francia?": "La capital de Francia es París.",
    "¿Cuánto es 2 + 2?": "2 + 2 es igual a 4.",
    "¿Cuál es el significado de la vida?": "Y tú?.",
    "¿Puedes ayudarme con matemáticas?": "Claro, puedo responder cuanto es 2 + 2.",
    "¿Cuál es tu color favorito?": "El rojo, el color de la sangre de mis enemigos.",
    "¿Puedes aprender nuevas preguntas?": "Por ahora, solo respondo con las preguntas predefinidas."
}

# Extraer solo las preguntas y preprocesarlas
questions = list(qa_pairs.keys())
processed_questions = [preprocess_text(q) for q in questions]

# Vectorizar las preguntas con TF-IDF
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(processed_questions)

def get_response(user_input):
    # Encuentrar la mejor respuesta basada en similitud de coseno entre la pregunta del usuario y las predefinidas.

    processed_input = preprocess_text(user_input)
    user_vector = vectorizer.transform([processed_input])
    similarities = cosine_similarity(user_vector, question_vectors)
    max_similarity = np.max(similarities)
    
    if max_similarity >= 0.75:
        best_match_index = np.argmax(similarities)
        return qa_pairs[questions[best_match_index]]
    else:
        return "No entiendo tu pregunta, intenta reformularla."

# Bucle principal del chatbot
print("Chatbot: ¡Hola! Puedes hacerme preguntas o escribir 'salir' para terminar.")
while True:
    user_input = input("Tú: ")
    if user_input.lower() == "salir":
        print("Chatbot: ¡Hasta luego!")
        break
    response = get_response(user_input)
    print(f"Chatbot: {response}")
