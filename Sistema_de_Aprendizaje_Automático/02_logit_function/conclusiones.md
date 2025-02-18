# Conclusiones


### **Determinación de Factores Clave**  
Las características más relevantes en la decisión de aprobación son:
1. **Edad (-0.0287)** – Un coeficiente negativo sugiere que a mayor edad, menor probabilidad de aprobación.
2. **Deudas Activas (-0.0226)** – También tiene un impacto negativo, indicando que más deudas reducen la posibilidad de aprobación.
3. **Ingreso Anual (-0.0183)** – Aunque tiene menor peso que las anteriores, sigue siendo relevante; ingresos más altos pueden aumentar la probabilidad de aprobación.
4. **Puntaje de Crédito (-0.0019)** – Tiene un impacto casi nulo, lo que sugiere que no está influyendo significativamente en la decisión del modelo.

---

### **Limitaciones del Modelo**  
1. **Baja precisión y generalización**  
   - **Accuracy = 0.49**, apenas mejor que una clasificación aleatoria.  
   - **AUC-ROC = 0.49**, indicando que el modelo no diferencia bien entre clases.  
2. **Desbalance en Recall**  
   - **Clase "Aprobado" (recall = 0.64)**: Mejor identificación de aprobaciones.  
   - **Clase "Rechazado" (recall = 0.35)**: Mal desempeño en identificar rechazos.  
3. **Coeficientes pequeños**  
   - Ninguna variable parece predecir correctamente. Esto podría deberse a la falta de información relevante en el dataset o a la necesidad de transformar variables.  
4. **Posibles problemas con la escala de datos**  
   - Se usó estandarización con `StandardScaler()`, pero podría no ser la mejor opción si las variables no siguen una distribución normal.  

---

### **Aplicabilidad a la Empresa**
- **No es recomendable utilizar este modelo en una campaña real** sin mejoras.
- La baja precisión y el desequilibrio en la clasificación podrían generar errores en la aprobación/rechazo de clientes.
- Se necesita mejorar la discriminación entre clases antes de implementarlo en un entorno de producción.

---

### **Importancia de la Interpretabilidad**
- **Ventaja:** La regresión logística es altamente interpretable, permitiendo entender el impacto de cada variable.
- **Desventaja:** La baja efectividad del modelo limita su utilidad práctica.
- Antes de confiar en estos coeficientes, es fundamental mejorar la calidad del modelo.

---

### **Recomendaciones**
1. **Agregar más características** que puedan mejorar la predicción (ej. historial crediticio, antigüedad laboral).
2. **Manejar el desbalance de clases** con técnicas como ajuste de pesos (`class_weight='balanced'`) o recolección de más datos.
3. **Explorar modelos más complejos** como Random Forest, que pueden capturar relaciones no lineales.
4. **Revisar colinealidad** entre variables, ya que coeficientes pequeños pueden indicar redundancia o falta de información útil.