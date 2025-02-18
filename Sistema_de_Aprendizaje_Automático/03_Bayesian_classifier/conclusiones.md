# Conclusiones

## **Determinación de Factores Clave**
Los factores más relevantes en la clasificación de spam son:
1. **Contiene_Adjunto (0.0187)** → Indica que los correos con archivos adjuntos pueden estar ligeramente más relacionados con el spam.
2. **Contiene_Oferta (0.0165)** → Sugerencia de promociones o descuentos podría influir en la clasificación.
3. **Contiene_Enlace (0.0163)** → Presencia de enlaces en los correos, que suele asociarse con intentos de phishing o marketing agresivo.
4. **Longitud del correo (0.000007)** → Parece tener una **baja relevancia**, indicando que la extensión del correo no es un factor clave para la clasificación.

Sin embargo, las **importancias son muy bajas y cercanas entre sí**, lo que indica que el modelo no tiene una separación clara entre clases.

---

## **Limitaciones del Modelo**
1. **Desbalance de Clases**  
   - Hay **muchos más correos "No Spam" (34,837) que "Spam" (15,163)**.
   - Esto provoca que el modelo **aprenda a predecir solo la clase mayoritaria** (como se observa en la matriz de confusión).

2. **Problemas en la Clasificación**
   - **Recall en "Spam" es 0.00** → El modelo **nunca predice correos spam correctamente**.
   - **F1-Score en "Spam" es 0.00** → No está capturando patrones en los correos spam.
   - **AUC-ROC de 0.48** → Prácticamente aleatorio, lo que indica que el modelo no tiene un poder predictivo útil.

3. **Modelo No Generalizable**
   - Este tipo de modelo asume independencia entre variables, lo cual puede no ser válido en este caso.

---

## **Aplicabilidad a la Empresa**
**No es viable utilizar este modelo en una campaña real** porque:
- No predice correctamente la clase "Spam".
- Si se usa para filtrar correos en una campaña de marketing, podría dejar pasar correos no deseados y afectar la reputación de la empresa.
- La precisión en la clase mayoritaria ("No Spam") es aceptable, pero la incapacidad de detectar "Spam" lo hace **inutilizable en producción**.

---

## **Importancia de la Interpretabilidad**
El modelo **Multinomial Naive Bayes** es relativamente fácil de interpretar, ya que asigna probabilidades a cada clase en función de la frecuencia de las características en los datos. Esto permite:

- Comprender qué factores tienen mayor peso en la clasificación de correos como spam o no.
- Explicar a los responsables de marketing cómo influyen variables como presencia de enlaces, adjuntos o palabras clave en la detección de spam.
- Ajustar estrategias de filtrado de correos en función de la importancia de cada característica.


**Pero en este caso, la interpretabilidad no es útil** porque el modelo **no está funcionando bien**. Antes de analizar factores clave, es necesario mejorar la capacidad predictiva.  