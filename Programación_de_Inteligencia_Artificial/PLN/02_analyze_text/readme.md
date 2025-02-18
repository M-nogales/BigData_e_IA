```markdown
# Ejercicio 1: Tokenización y Análisis Morfológico
Separar un texto en palabras y analizar su estructura gramatical.

**Librerías necesarias:** `nltk`, `spaCy`

```python
# Texto de prueba
texto = "El procesamiento del lenguaje natural es una rama de la inteligencia artificial."
```

# Ejercicio 2: Reconocimiento de Entidades Nombradas (NER)
Identificar nombres de personas, lugares y organizaciones en un texto.

**Librerías necesarias:** `spaCy`

```python
# Texto de prueba
texto = "El fundador de Tesla, Elon Musk, ha invertido en inteligencia artificial."
```

# Ejercicio 3: Análisis de Sentimiento
Determinar si un texto tiene un sentimiento positivo, negativo o neutral.

**Librerías necesarias:** `textblob-es`

```python
# Texto de prueba
texto = "Me encanta aprender sobre inteligencia artificial, es fascinante."
```

# Ejercicio 4: Traducción Automática
Traducir un texto del español al inglés.

**Librerías necesarias:** `googletrans`

```python
# Texto de prueba
texto = "El aprendizaje profundo está revolucionando el procesamiento del lenguaje natural."
```

# Ejercicio 5: Reconocimiento de Voz
Convertir audio a texto usando reconocimiento de voz.

**Librerías necesarias:** `SpeechRecognition`

```python
# Cargar audio (debe ser un archivo WAV)
```

# Ejercicio 6: Generación de Texto con un Modelo Preentrenado (GPT-2)
Generar texto automáticamente a partir de una entrada inicial.

**Librerías necesarias:** `transformers`

```python
# Generar texto
entrada = "La inteligencia artificial está transformando el mundo porque"
```

# ENTREGA
Un fichero Python por cada uno de los ejercicios.

## PIP instalation
pip install textblob
pip install nltk spacy googletrans==4.0.0-rc1 SpeechRecognition transformers torch

py -3.12 -m pip install textblob nltk spacy googletrans==4.0.0-rc1 SpeechRecognition transformers torch

py -3.12 -m spacy download es_core_news_sm
