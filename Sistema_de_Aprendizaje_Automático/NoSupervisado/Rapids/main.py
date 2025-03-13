# 1. Cargar datos
from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import cudf

categories = ['sci.space', 'rec.sport.baseball', 'talk.politics.guns']
news = fetch_20newsgroups(subset='all', categories=categories, remove=('headers', 'footers', 'quotes'))
textos = news.data[:1000] # Usamos 1000 noticias para ejemplo rápido
etiquetas = news.target[:1000]

# 2. Convertir a cuDF DataFrame
df = cudf.DataFrame({'texto': textos, 'categoria': etiquetas})

# 3. Preprocessamiento (ejemplo básico: eliminar puntuación)
df['texto'] = df['texto'].str.replace('[^\w\s]', '', regex=True)

# 4. Extracción de características (TF-IDF)
tfidf = TfidfVectorizer()
X = tfidf.fit_transform(df['texto'].to_pandas())  # Convertir a pandas para scikit-learn
y = df['categoria'].to_pandas().values
# 5. Dividir datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Entrenar modelo
modelo = LogisticRegression(max_iter=1000)
modelo.fit(X_train, y_train)

# 7. Evaluar
predicciones = modelo.predict(X_test)
accuracy = accuracy_score(y_test, predicciones)
print(f"Accuracy: {accuracy:.4f}") # Accuracy: 0.8350