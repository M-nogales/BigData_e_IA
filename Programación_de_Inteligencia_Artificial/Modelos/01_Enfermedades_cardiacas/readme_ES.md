# Informe del ejercicio de Machine Learning 
**Nombre:** Manuel Nogales Serrano  
**Fecha:** 02/02/2025  

---

## 1. Análisis del Problema  
El objetivo de este ejercicio es predecir la presencia de enfermedad cardíaca (`enfermedad_cardiaca`) basándose en un conjunto de características clínicas. El conjunto de datos incluye variables como la edad, el sexo, la presión arterial, los niveles de colesterol, los niveles de glucosa, el índice de masa corporal (IMC), la actividad física, los hábitos de fumar, los antecedentes familiares y el estado de diabetes.  

### Descripción del Conjunto de Datos  
- **Nombre del Conjunto de Datos:** `Dataset_Enfermedades.csv`  
- **Características:** `edad`, `sexo`, `presion_sistolica`, `presion_diastolica`, `colesterol`, `glucosa`, `indice_masa_corporal`, `actividad_fisica`, `fumar`, `historia_familiar`, `diabetes`  
- **Variable Objetivo:** `enfermedad_cardiaca` (binaria: 0 = sin enfermedad, 1 = con enfermedad)  

El conjunto de datos se dividió en conjuntos de entrenamiento (80%) y prueba (20%) para evaluar el rendimiento de los modelos.  

```python
# Features:
X = health[['edad','sexo','presion_sistolica','presion_diastolica','colesterol','glucosa','indice_masa_corporal','actividad_fisica','fumar','historia_familiar','diabetes']]
# Target :
y = health['enfermedad_cardiaca']
# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

---

## 2. Modelos Aplicados  
Se aplicaron los siguientes modelos de machine learning al conjunto de datos:  
1. **Regresión Logística (Logistic Regression)**  
2. **Bosque Aleatorio (Random Forest)**  
3. **Árbol de Decisión (Decision Tree)**  
4. **Máquina de Vectores de Soporte (Support Vector Machine, SVM)**  

Cada modelo fue entrenado y evaluado utilizando las siguientes métricas:  
- **Accuracy**: Proporción de instancias clasificadas correctamente.  
- **Recall**: Capacidad para identificar todas las instancias relevantes (verdaderos positivos).  
- **F1-Score**: Media armónica de la precisión y el recall.  
- **AUC-ROC**: Área bajo la curva ROC, que mide la capacidad del modelo para distinguir entre clases.  

---

## 3. Resultados e Interpretación  

### 3.1 Logistic Regression
```python
# Data normalization
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train the logistic regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
y_pred_prob = model.predict_proba(X_test)[:, 1]
```  
**Resultados:**  
- **Accuracy:** 0.91  
- **Recall:** 0.95  
- **F1-Score:** 0.94  
- **AUC-ROC:** 0.96  

**Interpretación:**  
El modelo "logistic Regression" obtuvo un alto Accuracy (0.91) y Recall (0.95), lo que indica que es efectivo para predecir la enfermedad cardíaca e identificar la mayoría de los casos positivos. El F1-Score (0.94) y el AUC-ROC (0.96) confirman su buen rendimiento, sugiriendo que generaliza bien con datos no vistos. Este modelo es una base confiable para esta tarea de clasificación.  

---

### 3.2 Random Forest
```python
# Create the Random Forest model with 100 trees
rf_model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
rf_model.fit(X_train, y_train)
''' RandomForestClassifier params:
n_estimators=100: indicates the number of trees in the forest (100 in this case).
max_depth=5: Limits the depth of the tree to 5 levels to prevent overfitting.
random_state=42: Ensures reproducibility of the results.
fit(X_train, y_train): Trains the model on the training data.
'''

# predictions
y_pred = rf_model.predict(X_test)
y_pred_prob = rf_model.predict_proba(X_test)[:, 1]
```  
**Resultados:**  
- **Accuracy:** 0.89  
- **Recall:** 1.00  
- **F1-Score:** 0.93  
- **AUC-ROC:** 1.00  

**Interpretación:**  
El modelo "Random Forest" obtuvo un Recall perfecto (1.00) y un AUC-ROC perfecto (1.00), lo que indica que es excelente para identificar todos los casos positivos y distinguir entre clases. Sin embargo, su Accuracy (0.89) es ligeramente inferior al de "Logistic Regression", lo que podría deberse a un sobreajuste o a la complejidad del modelo. A pesar de esto, sigue siendo una opción robusta para este problema.  

---

### 3.3 Decision Tree  
```python
# Create the Decision Tree model
tree_clf = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)
# example using all the parameters
# tree_clf = DecisionTreeClassifier(
#     criterion='entropy', #gini, entropy
#     max_depth=6,  # Limit the depth of the tree
#     min_samples_split=10,  # Minimum samples required to split a node
#     min_samples_leaf=5,  # Minimum samples required to be at a leaf node
#     class_weight='balanced',  # Handle class imbalance
#     max_features='sqrt',  # Consider only a subset of features at each split
#     random_state=42,  # For reproducibility
#     min_impurity_decrease=0.01,  # Minimum impurity decrease for a split
#     ccp_alpha=0.01  # Prune tree if needed
# )

tree_clf.fit(X_train, y_train)

# Predictions
y_pred = tree_clf.predict(X_test)
y_pred_prob = tree_clf.predict_proba(X_test)[:, 1]
```
**Resultados:**  
- **Accuracy:** 0.77  
- **Recall:** 0.90  
- **F1-Score:** 0.85  
- **AUC-ROC:** 0.80  

**Interpretación:**  
El modelo "Decision Tree" obtuvo un Accuracy moderado (0.77) y un Recall alto (0.90), lo que indica que puede identificar la mayoría de los casos positivos pero tiene dificultades con la precisión general. El F1-Score (0.85) y el AUC-ROC (0.80) sugieren que tiene un rendimiento razonable, pero es menos efectivo que "Logistic Regression" o "Random Forest". Su simplicidad lo hace interpretable, pero puede limitar su poder predictivo.  

---

### Support Vector Machine (SVM)  
```python
# Data normalization
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# train the SVM model
model = SVC(kernel='rbf', C=1.0, probability=True, gamma='scale',class_weight='balanced')
model.fit(X_train, y_train)
'''
Params:
kernel='rbf': Kernel function used in the algorithm (Radial Basis Function), suitable for non-linear data.
C=1.0: Regularization parameter, controls the trade-off between smooth decision boundary and classifying the training points correctly.
gamma='scale': Controls the influence of a single training point (auto value based on features).
#! probability=True: Enable the probability estimates, needed for AUC-ROC calculation.
'''
# Predictions
y_pred = model.predict(X_test)
y_pred_prob = model.predict_proba(X_test)[:, 1]
```

**Resultados:**  
- **Accuracy:** 0.91  
- **Recall:** 0.91  
- **F1-Score:** 0.94  
- **AUC-ROC:** 0.97  

**Interpretación:**  
El modelo SVM obtuvo un Accuracy alto y un Recall alto (0.91) ambos, lo que lo convierte en uno de los modelos con mejor rendimiento. Su F1-Score (0.94) y AUC-ROC (0.97) confirman su fuerte capacidad para generalizar y distinguir entre clases. Sin embargo, su coste computacional puede ser mayor en comparación con otros modelos, lo que es una desventaja frente a su rendimiento.  

---

## 4. Comparación de Modelos  
Comparación de las métricas de rendimiento para todos los modelos:  

| Modelo               | Accuracy | Recall | F1-Score | AUC-ROC |  
|----------------------|----------|--------|----------|---------|  
| Regresión Logística  | 0.91     | 0.95   | 0.94     | 0.96    |  
| Bosque Aleatorio     | 0.89     | 1.00   | 0.93     | 1.00    |  
| Árbol de Decisión    | 0.77     | 0.90   | 0.85     | 0.80    |  
| SVM                  | 0.91     | 0.91   | 0.94     | 0.97    |  

**Visualización:**  
![Logistic regresion](imgs/metrics_logistic.png)
![Random forest](imgs/metrics_random_forest.png)
![SVM](imgs/metrics_svm.png)
![Decission tree](imgs/metrics_decision_tree.png)

**Interpretación:**  
La comparación muestra que **"Logistic Regression"** y **SVM** son los modelos con mejor rendimiento, con un Accuracy, Recall, F1-Score y AUC-ROC altos. **"Random Forest"** también tiene un buen rendimiento, especialmente en Recall y AUC-ROC, pero su Accuracy es ligeramente inferior. El modelo de **"Decision Tree"** se queda atrás en todas las métricas, probablemente debido a su simplicidad y su potencial de sobreajuste. En general, "Logistic Regression" y SVM son las opciones más confiables para este conjunto de datos.

---

## 5. Conclusión  
Basándonos en el análisis, **"Logistic Regression"** y **SVM** son los modelos más efectivos para predecir la enfermedad cardíaca en este conjunto de datos. Ambos modelos obtuvieron un Accuracy, Recall y AUC-ROC altos, demostrando su capacidad para generalizar bien e identificar casos positivos. **"Random Forest"** también tuvo un buen rendimiento, pero podría requerir ajustes para mejorar su Accuracy. El modelo de **"Decision Tree"**, aunque interpretable, es menos efectivo y podría no ser adecuado para esta tarea sin una optimización adicional.  

---

## 6. Referencias  
- Librerías: `pandas`, `matplotlib`, `scikit-learn`  
