import nltk
import string
import collections
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.corpus import stopwords

# Asegurar que los recursos de nltk están disponibles
nltk.download('stopwords')

# Archivo de texto
with open("odyssey.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Preprocesamiento del texto
text = text.lower()  # Convertir a minúsculas
text = text.translate(str.maketrans("", "", string.punctuation))  # Eliminar puntuación

# Tokenización y eliminación de stopwords
words = text.split()
stop_words = set(stopwords.words('english'))  # Stopwords en inglés
filtered_words = [word for word in words if word not in stop_words]

# Contar la frecuencia de palabras
word_freq = collections.Counter(filtered_words)
print("Palabras más comunes:", word_freq.most_common(10))

# Generar la nube de palabras
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)
# Mostrar y guardar la imagen
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig("nube_palabras.png", format="png")
plt.show()

print("Proceso finalizado. Se ha generado 'nube_palabras.png'")
