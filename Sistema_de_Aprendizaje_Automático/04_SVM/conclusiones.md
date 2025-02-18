# Conclusiones

Fraude
0    28063
1     6937
Name: count, dtype: int64
🔹 Confusion Matrix:
[[3709 4788]
 [ 916 1087]]
🔹 Accuracy: 0.46
🔹 Recall: 0.54
🔹 F1-Score: 0.28
🔹 AUC-ROC: 0.51

Classification Report:
               precision    recall  f1-score   support

  Legitimate       0.80      0.44      0.57      8497 
  Fraudulent       0.19      0.54      0.28      2003 

    accuracy                           0.46     10500 
   macro avg       0.49      0.49      0.42     10500 
weighted avg       0.68      0.46      0.51     10500 


## **Determinación de Factores Clave**
Los **factores clave** en la detección de fraude podrían ser características como:
  - **Monto de la transacción**: Las transacciones fraudulentas podrían estar asociadas con montos inusualmente altos o inusuales en comparación con la actividad previa del usuario.
  - **Frecuencia de uso**: Las transacciones fuera de un patrón de frecuencia normal (por ejemplo, transacciones en un corto período de tiempo) podrían ser indicativos de fraude.
  - **Sospechosidad de la transacción**: Si se ha identificado alguna regla interna que clasifique una transacción como sospechosa, esto podría ser un factor importante.
  
El hecho de que el modelo tenga dificultades para identificar correctamente las transacciones fraudulentas sugiere que hay un **desbalance en las clases**, ya que la clase fraude tiene más de 4 veces la cantidad de transacciones fraudulentas.

#### 2. **Desempeño del Modelo**
- **Precisión global**: La precisión global del modelo es **0.46**, lo que indica que el modelo no está funcionando de manera efectiva en general. Una precisión de 0.46 es bastante baja, lo que significa que el modelo está cometiendo muchos errores, especialmente en la clasificación de las transacciones fraudulentas.
- **Recall para la clase de fraude**: El recall de **0.54** para las transacciones fraudulentas sugiere que el modelo detecta alrededor de la mitad de las transacciones fraudulentas, pero sigue perdiendo una proporción significativa de ellas.
- **F1-Score de la clase de fraude**: El F1-Score de **0.28** es bajo, lo que refleja una mala capacidad del modelo para encontrar un equilibrio entre la precisión y el recall en la clase fraudulenta.
- **AUC-ROC de 0.51**: Este valor es muy cercano a 0.5, lo que significa que el modelo tiene un desempeño cercano al azar en la clasificación. Esto indica que el modelo no está distinguiendo bien entre las clases de fraude y no fraude.

#### 3. **Posibles Mejoras al Modelo**

- **Balanceo de clases**: El modelo muestra un **desbalance de clases** evidente (muchas más transacciones legítimas que fraudulentas). Algunas técnicas para abordar esto incluyen:
  - **Sobremuestreo** de las transacciones fraudulentas (por ejemplo, con técnicas como SMOTE).
  - **Submuestreo** de las transacciones legítimas.
  
- **Optimización de Hiperparámetros**: El modelo podría mejorar los resultados ajustando el valor de `C` o `gamma` en el SVM.
  
- **Otros Algoritmos**: Dado que el modelo de SVM no está dando buenos resultados, podría ser útil comparar con otros algoritmos, como:
  - **Árboles de decisión** o **Random Forest**, que son menos sensibles al desbalanceo de clases.
  - **Redes neuronales** podría manejar mejor el desbalanceo de clases y mejorar la capacidad predictiva.
  
- **Características adicionales**: Se podría considerar agregar más características que capturen patrones relacionados con fraudes, como el historial de transacciones del cliente o la geolocalización de las mismas.

#### 4. **Aplicabilidad a un Sistema Real**
- Para que el modelo sea útil en un **sistema real de detección de fraudes**, se deben alcanzar niveles de desempeño más altos, especialmente en cuanto a la **recuperación de fraudes** (recall). Un modelo que tiene un recall bajo para la clase de fraude podría estar perdiendo demasiados casos fraudulentos, lo que es inaceptable en aplicaciones como el monitoreo de transacciones bancarias en tiempo real.
- Para un sistema de detección de fraudes en tiempo real, se necesitarían **modelos que minimicen tanto los falsos positivos como los falsos negativos**, lo que requiere un modelo más robusto y optimizado que este.