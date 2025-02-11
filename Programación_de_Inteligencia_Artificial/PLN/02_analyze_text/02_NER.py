import spacy

# Cargar el modelo en español de spaCy
nlp = spacy.load("es_core_news_lg")

# Texto de prueba
texto = "El fundador de Tesla Inc, Elon Musk, ha invertido en inteligencia artificial."

# Procesar el texto con spaCy
doc = nlp(texto)

# Imprimir entidades nombradas
print("Entidades reconocidas:")
for ent in doc.ents:
    print(f"{ent.text} → {ent.label_}")

# Explicación de las etiquetas
print("\nExplicación de etiquetas:")
for ent in doc.ents:
    print(f"{ent.text}: {spacy.explain(ent.label_)}")
