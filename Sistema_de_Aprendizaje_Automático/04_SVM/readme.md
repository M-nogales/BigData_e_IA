## PROBLEMA: Detección de Fraude en Transacciones Bancarias usando SVM

Una entidad bancaria está interesada en desarrollar un sistema automático que le ayude a detectar transacciones fraudulentas. Para ello, ha recopilado un conjunto de datos con información sobre diversas transacciones realizadas por sus clientes.

Cada transacción está caracterizada por atributos como el monto, el tipo de transacción, la frecuencia de transacciones del usuario, el país de origen y si la transacción es sospechosa según reglas internas del banco.

El objetivo es desarrollar un modelo de Máquina de Vectores de Soporte (SVM) que permita predecir si una transacción es fraudulenta (1) o legítima (0) en función de estas características.

### Datos
Los datos están organizados de la siguiente manera:

| ID | Monto | Frecuencia_Us | Tipo_Transacción  | País    | Sospechosa  | Fraude  |
|----|-------|---------------|-------------------|--------|------------|--------|
| 1  | 500   | 3             | Compra Online     | USA    | Sí         | 1      |
| 2  | 30    | 20            | Retiro ATM        | España | No         | 0      |
| 3  | 5000  | 1             | Transferencia     | Rusia  | Sí         | 1      |
| ...| ...   | ...           | ...               | ...    | ...        | ...    |

Se debe desarrollar un modelo de SVM en Python que permita clasificar transacciones como fraudulentas o legítimas en función de sus características. Los datos disponibles se adjuntan en el fichero `fraude_data.csv`.

### Requerimientos
- Generar el código en Python utilizando el modelo de Máquina de Vectores de Soporte (SVM).
- Indicar las conclusiones obtenidas tras el estudio.

## CONCLUSIONES

### Factores Clave para la Detección de Fraude
- Evaluar qué características (monto, frecuencia de uso, si la transacción es sospechosa) tienen mayor peso en la detección de fraude.
- Si el modelo se apoya en transacciones de alto monto o con baja frecuencia para clasificar fraudes, se debe considerar la posibilidad de refinar los datos.

### Desempeño del Modelo
- Si la precisión general es alta, el modelo es eficaz para predecir fraudes.
- Si la precisión en la clase de fraude es baja, el modelo podría estar pasando por alto transacciones fraudulentas.

### Posibles Mejoras al Modelo
- Balanceo de clases.
- Optimización de hiperparámetros.
- Comparación con otros algoritmos.

### Aplicabilidad a un Sistema Real
- Evaluar si el modelo es suficientemente preciso para integrarse en un sistema de detección de fraudes en tiempo real.