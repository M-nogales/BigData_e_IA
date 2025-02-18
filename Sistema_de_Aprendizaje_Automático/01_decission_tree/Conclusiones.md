# Conclusiones

### **Determinación de Factores Clave**  
Los factores más relevantes en la decisión de compra son:  
1. **Ingreso Anual (47%)** – Es la característica con mayor peso, por lo que la capacidad económica del usuario es clave en la decisión de compra.
2. **Edad (22.4%)** – También tiene un impacto significativo, posiblemente porque ciertos rangos de edad tienen mayor disposición o capacidad de compra.
3. **Tiempo en Web (20.4%)** – Sugiere que los usuarios que pasan más tiempo navegando tienen una mayor probabilidad de compra.
4. **Número de Compras (0.0%)** – Un historial de compras previas puede ser un buen predictor de futuras compras.
5. **Frecuencia de Visitas (0.99%)** – Aunque menos influyente, sigue siendo relevante, indicando que los clientes recurrentes pueden tener mayor intención de compra.

---

### **Limitaciones del Modelo**
1. **Precisión baja (Accuracy = 0.57)**
   - Apenas mejor que una clasificación aleatoria (0.57).
2. **Desequilibrio en Recall y F1-Score**
   - El modelo tiene dificultades para identificar correctamente las clases (especialmente la clase "No compra", con un recall de 0.38).
3. **AUC-ROC = 0.57**
   - Indica que el modelo no es mejor que una clasificación aleatoria.
4. **Sesgo en los datos**
   - El dataset no es representativo (por tamaño y distribución), el modelo no puede capturar bien la realidad.

---

### **Aplicabilidad a la Empresa**
- **No es recomendable usar este modelo en una campaña real** en su estado actual.
- Necesita mejoras en precisión y capacidad de generalización.
- Se podría probar con **técnicas de balanceo de clases** (como SMOTE o reponderación), o **uso de otro modelo** como Random Forest.

---

### **Importancia de la Interpretabilidad**
- **Ventaja:** El Árbol de Decisión es fácil de interpretar, permitiendo a los equipos de marketing entender qué factores influyen en la compra.
- **Problema:** Dada la baja precisión del modelo, confiar en sus insights podría dar malos resultados.
- Se recomienda mejorar la calidad del modelo antes de tomar decisiones estratégicas basadas en él.

---

### **Recomendaciones**
1. **Equilibrar las clases** con técnicas como oversampling o undersampling.
2. **Explorar otros modelos** Random Forest.
3. **Realizar validación cruzada** para evaluar la estabilidad del modelo.
4. **Aumentar el tamaño del dataset** si es posible, para mejorar representatividad.