# PROBLEMA: Clasificación de Clientes para una campaña de Marketing

Una empresa de comercio electrónico desea optimizar su estrategia de marketing dirigiendo campañas específicas a diferentes tipos de clientes. Para ello, ha recopilado datos históricos de clientes, incluyendo información como su edad, ingresos anuales, historial de compras y nivel de interacción con la plataforma (número de compras, tiempo en la web, frecuencia de visitas, etc.).

Se desea construir un modelo de clasificación basado en Árboles de Decisión que ayude a predecir si un cliente es propenso a comprar un producto específico después de recibir una campaña de marketing.

Los datos están estructurados de la siguiente manera:

| Cliente_ID | Edad | Ingreso_Anual | Frecuencia_Visitas | Número_Compras | Tiempo_En_Web | Compra |
|------------|------|---------------|--------------------|----------------|---------------|--------|
| 1          | 25   | 30,000        | 5                  | 2              | 15            | No     |
| 2          | 40   | 60,000        | 2                  | 5              | 20            | Sí     |
| 3          | 35   | 45,000        | 3                  | 3              | 10            | No     |


Los datos disponibles se adjuntan en el fichero `clientes_marketing.csv`.

Generar el código Python utilizando algoritmo de Árbol de Decisión

## CONCLUSIONES

### Determinación de Factores Clave
Analizar cuáles son las características más relevantes en la decisión de compra según la estructura del árbol de decisión.

### Limitaciones del Modelo
Reflexionar sobre posibles sesgos en los datos (por ejemplo, si el conjunto de datos es pequeño o no representativo).
Considerar si el árbol de decisión es demasiado profundo o poco generalizable.

### Aplicabilidad a la Empresa
Evaluar si el modelo es suficientemente preciso para ser utilizado en una campaña real.

### Importancia de la Interpretabilidad
Un Árbol de Decisión es fácil de interpretar, lo que permite a los responsables de marketing entender qué factores influyen en las decisiones de los clientes.
Esto facilita la toma de decisiones estratégicas para futuras campañas.

## Entrega
- Fichero Python con el desarrollo del código y del algoritmo.
- PDF indicando el apartado de las conclusiones.
