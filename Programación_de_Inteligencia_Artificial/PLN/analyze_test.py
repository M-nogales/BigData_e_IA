import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.util import bigrams
import matplotlib.pyplot as plt

# 
nltk.download('stopwords') # Stopwords (palabras vacías)

with open('quijote.txt', 'r', encoding='utf-8') as file:
    don_quijote_text = file.read()

with open('odyssey.txt', 'r', encoding='utf-8') as file:
    the_odyssey_text = file.read()

# Tokenizar los textos
don_quijote_tokens = word_tokenize(don_quijote_text.lower())  # español
odyssey_tokens = word_tokenize(the_odyssey_text.lower())  # inglés

# Eliminar stopwords
stopwords_en = set(stopwords.words('english'))
stopwords_es = set(stopwords.words('spanish'))

don_quijote_tokens_clean = [word for word in don_quijote_tokens if word.isalpha() and word not in stopwords_es]
the_odyssey_clean = [word for word in odyssey_tokens if word.isalpha() and word not in stopwords_en]


# Análisis de frecuencia
fdist_en = FreqDist(the_odyssey_clean)
fdist_es = FreqDist(don_quijote_tokens_clean)

# Mostrar las palabras más frecuentes
print("Palabras más comunes en inglés:", fdist_en.most_common(10))
print("Palabras más comunes en español:", fdist_es.most_common(10))

# Graficar frecuencia
fdist_en.plot(20, title="Frecuencia de palabras en inglés")
plt.show()
fdist_es.plot(20, title="Frecuencia de palabras en español")
plt.show()

# longitud de palabras
word_lengths_en = [len(word) for word in the_odyssey_clean]
word_lengths_es = [len(word) for word in don_quijote_tokens_clean]

plt.subplot(1, 2, 1)
plt.hist(word_lengths_en, bins=range(1, max(word_lengths_en) + 1), alpha=0.75, color='blue', edgecolor='black')
plt.title("Distribución de longitudes de palabras en inglés")
plt.xlabel("Longitud de palabra")
plt.ylabel("Frecuencia")

plt.subplot(1, 2, 2)
plt.hist(word_lengths_es, bins=range(1, max(word_lengths_es) + 1), alpha=0.75, color='red', edgecolor='black')
plt.title("Distribución de longitudes de palabras en español")
plt.xlabel("Longitud de palabra")
plt.ylabel("Frecuencia")

plt.tight_layout()
plt.show()

# Análisis de bigramas (pares de palabras más comunes)
bigrams_en = bigrams(the_odyssey_clean)
bigrams_es = bigrams(don_quijote_tokens_clean)

fdist_bigrams_en = FreqDist(bigrams_en)
fdist_bigrams_es = FreqDist(bigrams_es)

print("\nBigramas más comunes en inglés:")
print(fdist_bigrams_en.most_common(10))

print("\nBigramas más comunes en español:")
print(fdist_bigrams_es.most_common(10))