from googletrans import Translator

# Texto de prueba
texto = "El aprendizaje profundo está revolucionando el procesamiento del lenguaje natural."

# Crear un objeto traductor
translator = Translator()

# Traducir el texto
traduccion = translator.translate(texto, src='es', dest='en')

# Imprimir la traducción
print(f"Texto original: {texto}")
print(f"Traducción al inglés: {traduccion.text}")

# podemos combinar el ejercicio anterior con este y obtener
# la traducción para analizar el sentimiento en inglés con TextBlob
from textblob import TextBlob

# Texto de prueba
texto = "Me encanta aprender sobre inteligencia artificial, es fascinante."

#traducir el texto
traduccion = translator.translate(texto, src='es', dest='en')

# Crear un objeto TextBlob
blob = TextBlob(traduccion.text)

# Analizar el sentimiento
sentimiento = blob.sentiment

# Determinar el tipo de sentimiento
if sentimiento.polarity > 0:
    tipo_sentimiento = "Positivo"
elif sentimiento.polarity < 0:
    tipo_sentimiento = "Negativo"
else:
    tipo_sentimiento = "Neutral"

# Imprimir resultados
print("\nAnalisis del sentimiento:")
print(f"Sentimiento: {tipo_sentimiento}")
print(f"Polaridad: {sentimiento.polarity}, Subjetividad: {sentimiento.subjectivity}")
