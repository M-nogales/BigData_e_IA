# Librerías necesarias
import nltk
import spacy

# Descargar recursos de NLTK (solo la primera vez)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('universal_tagset')

# Cargar el modelo de lenguaje en español de spaCy
nlp = spacy.load("es_core_news_sm")

sample_text = "El procesamiento del lenguaje natural es una rama de la inteligencia artificial."


# --- Tokenización y Análisis Morfológico con NLTK ---
print("--- Análisis con NLTK ---")

# Tokenización
tokens_nltk = nltk.word_tokenize(sample_text, language='spanish')
print("Tokens (NLTK):", tokens_nltk)


# Análisis Morfológico con NLTK NO TIENE ETIQUETADO EN ESPAÑOL,
# por lo que da resultados imprecisos
pos_tags = nltk.pos_tag(tokens_nltk, tagset='universal')

print("Etiquetas POS (NLTK):",pos_tags)


#Análisis Morfológico con spaCy
print("\n--- Análisis con spaCy ---")

doc = nlp(sample_text)

# Tokenización y análisis morfológico
print("Tokens (spaCy):", [token.text for token in doc])
print("\n--- Etiquetas POS con spaCy ---")
print("Etiquetas POS (spaCy):", [(token.text, token.pos_) for token in doc])