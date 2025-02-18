from textblob import TextBlob

# Texto de prueba
# No existe TextBlob en español, en inglés, frances o aleman
# textbolb-fr, textblob-de

# texto = "Me encanta aprender sobre inteligencia artificial, es fascinante."

texto = "I love learning about artificial intelligence, it's fascinating."

# Crear un objeto TextBlob
blob = TextBlob(texto)

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
print(f"Sentimiento: {tipo_sentimiento}")
print(f"Polaridad: {sentimiento.polarity}, Subjetividad: {sentimiento.subjectivity}")
