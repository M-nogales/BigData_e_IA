## **¿Cómo varía el umbral de detección con diferentes hiperparámetros?**
### **Hiperparámetros Clave que Afectan el Umbral**
1. **`contamination`**  
   - Es el **factor crítico**: define qué porcentaje de los datos se etiquetarán como anomalías.  
   - Si aumentas `contamination`, el umbral se relaja (detecta más puntos, incluyendo potenciales falsos positivos).  
   - Si reduces `contamination`, el umbral se vuelve conservador (solo detecta las anomalías más evidentes).  

2. **`n_estimators` y `max_samples`**  
   - Afectan la **calidad de la estimación** del umbral:  
     - Más árboles (`n_estimators`) y muestras (`max_samples`) -> Mejor estimación de las regiones "aislables" (anomalías).  
     - Menos árboles/muestras -> Umbral basado en una representación incompleta de los datos.  

3. **`max_features`**  
   - Determina cuántas características se usan para construir los árboles:  
     - Si usas pocas features, el umbral puede ignorar variables clave para detectar anomalías.  

---

### **Explicación de cada hiperparámetro**
#### `n_estimators` (default = `100`)  
- Número de árboles del bosque.  
- **Más árboles** -> Mejor generalización, pero más costoso.  
- **Menos árboles** -> Menor precisión, pero más rápido.  

#### `max_samples` (default = `"auto"`)  
- Cantidad de muestras usadas para entrenar cada árbol.  
- `"auto"` -> Usa `min(256, n_muestras)`, lo que equilibra rendimiento y precisión.  
- Si se define un número entero -> Ese número exacto de muestras se usa en cada árbol.  
- Si se define un valor entre `(0,1]` -> Se toma un porcentaje del dataset.  

#### `contamination` (default = `"auto"`)  
- Proporción esperada de anomalías en los datos.  
- `"auto"` -> Estima la proporción basándose en la distribución de datos.  
- Valor flotante `(0,1]` -> Define manualmente la fracción de anomalías (ej. `0.05` significa 5% de anomalías).  

#### `max_features` (default = `1`)  
- Porcentaje de características (`features`) utilizadas en cada árbol.  
- `1` -> Usa todas las características.  
- Valores menores a `1` -> Usa solo una fracción de las características, lo que puede ayudar en datasets de alta dimensión para mejorar la velocidad.  

#### `bootstrap` (default = `False`)  
- Si `True`, usa **muestreo con reemplazo** para entrenar cada árbol.  
- Si `False`, cada árbol usa un subconjunto de datos sin reemplazo.  
- Puede mejorar la estabilidad del modelo en ciertos datasets, pero incrementa el costo.  

#### `n_jobs` (default = `None`)  
- Controla el número de CPU usados en paralelo para entrenar el modelo.  
- `None` -> Usa un solo núcleo.  
- `-1` -> Usa todos los núcleos disponibles.  
- Número entero positivo -> Usa esa cantidad específica de núcleos.  

#### `random_state` (default = `None`)  
- Controla la aleatoriedad del modelo.  
- Si se fija un número (`random_state=42`), los resultados serán **reproducibles**.  
- Si es `None`, los resultados pueden variar en cada ejecución.  

#### `verbose` (default = `0`)  
- Controla la cantidad de información impresa en la consola.  
- `0` -> No muestra nada.  
- `1` o superior -> Muestra más detalles del proceso de entrenamiento.  

#### `warm_start` (default = `False`)  
- Si `True`, permite reutilizar los árboles entrenados cuando se ajusta el modelo con nuevos datos.  
- Si `False`, cada ejecución del modelo comienza desde cero.  

---

### **¿Cómo afectan estos hiperparámetros al modelo?**
| Hiperparámetro  |           Bajo Valor           |              Alto Valor             |
|-----------------|--------------------------------|-------------------------------------|
| `n_estimators`  | Rápido, pero menos preciso     | Más preciso, pero más lento         |
| `max_samples`   | Más ruido, menos estabilidad   | Menos ruido, más robusto            |
| `contamination` | Menos anomalías detectadas     | Más anomalías detectadas            |
| `max_features`  | Menos preciso, pero más rápido | Más preciso, pero más lento         |
| `bootstrap`     | Modelos más rápidos            | Modelos más estables, pero costosos |
