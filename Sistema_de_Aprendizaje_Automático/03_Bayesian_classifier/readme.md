# PROBLEMA: Clasificación de Correos Electrónicos para Detección de Spam

Una empresa de seguridad informática desea implementar un sistema automático para clasificar correos electrónicos y detectar si son spam o no spam. Para ello, han recopilado datos de correos electrónicos etiquetados, donde cada correo contiene información sobre ciertas palabras clave, la cantidad de enlaces en el mensaje y si incluye archivos adjuntos.

El objetivo es desarrollar un modelo de Clasificador Bayesiano Ingenuo que permita predecir si un nuevo correo electrónico es spam (1) o no spam (0) en función de sus características.

Los datos están organizados de la siguiente manera:

| Correo_ID | Palabras_Clave | Cantidad_Enlaces | Tiene_Adjuntos | Es_Spam |
|-----------|----------------|------------------|----------------|---------|
| 1         | oferta, gratis | 3                | Sí             | 1       |
| 2         | reunión, informe| 1                | No             | 0       |
| 3         | descuento, compra| 2              | Sí             | 1       |

Implementar un Clasificador Bayesiano Ingenuo en Python para predecir si un correo electrónico es spam o no spam, basado en características textuales y estructurales del correo.

Los datos disponibles se adjuntan en el fichero `spam_detection_data.csv`.

Generar el código Python utilizando el Clasificador Bayesiano


## CONCLUSIONES

### Determinación de Factores Clave para la Clasificación
Analizar qué características (ofertas, enlaces, adjuntos o longitud del correo) tienen más peso en la decisión del modelo.

### Evaluación del Desempeño del Modelo
Evaluar la precisión del modelo y su capacidad para distinguir entre spam y no spam.

### Posibles Mejoras al Modelo
Identificar limitaciones del modelo y sugerir mejoras, como la inclusión de más características o el uso de técnicas de preprocesamiento más avanzadas.

### Aplicabilidad a un Sistema Real
Evaluar si el modelo es suficientemente preciso para ser utilizado en un entorno real.

## Entrega
- Fichero Python con el desarrollo del código y del algoritmo.
- PDF indicando el apartado de las conclusiones.
