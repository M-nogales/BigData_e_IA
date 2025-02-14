# PROBLEMA: Evaluación de Solicitudes de Crédito

Una entidad financiera desea mejorar su proceso de evaluación de solicitudes de crédito. Para ello, ha recopilado datos históricos de clientes que han solicitado un crédito y si su solicitud fue aprobada o rechazada.

Se pretende desarrollar un modelo de Regresión Logística (LOGIT) que ayude a predecir si un nuevo solicitante tiene probabilidades de obtener la aprobación de su crédito en función de características como su edad, ingresos, número de deudas activas y puntaje de crédito.

Los datos están estructurados de la siguiente manera:

| Cliente_ID | Edad | Ingreso_Anual | Deudas_Activas | Puntaje_Credito | Aprobado |
|------------|------|---------------|----------------|-----------------|----------|
| 1          | 30   | 35,000        | 2              | 650             | No       |
| 2          | 45   | 70,000        | 0              | 750             | Sí       |
| 3          | 25   | 28,000        | 3              | 600             | No       |

El objetivo es desarrollar un modelo de Regresión Logística (LOGIT) en Python para predecir si una solicitud de crédito será aprobada (1) o rechazada (0) con base en las características del solicitante.

Los datos disponibles se adjuntan en el fichero `credit_approval_data.csv`.

Generar el código Python utilizando algoritmo LOGIT

## CONCLUSIONES

### Factores Clave en la Aprobación de Crédito
Analizar cuáles son las variables más influyentes en la aprobación del crédito.

### Desempeño del Modelo
Evaluar si la precisión obtenida es aceptable para su uso en una institución financiera.
Identificar si el modelo tiene problemas de falsos positivos (aprobar créditos que deberían ser rechazados) o falsos negativos (rechazar clientes que sí deberían recibir crédito).

### Limitaciones y Posibles Mejoras
Evaluar si el modelo es suficientemente preciso para ser utilizado en una campaña real. Sugerir mejoras.

## Entrega
- Fichero Python con el desarrollo del código y del algoritmo.
- PDF indicando el apartado de las conclusiones.
