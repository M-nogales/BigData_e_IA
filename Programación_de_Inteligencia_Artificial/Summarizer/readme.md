# Actividad Teórica UD04
## Preguntas:

1. **Diferencia entre cinemática directa e inversa en un robot manipulador:**
   - **Cinemática directa**: Determina la posición y orientación del efector final del robot a partir de los valores conocidos de las articulaciones (ángulos o desplazamientos).
   - **Cinemática inversa**: Calcula los valores de las articulaciones necesarios para alcanzar una posición y orientación deseadas del efector final. Es más compleja y puede tener múltiples soluciones o ninguna.

---

2. **Principales problemas que pueden afectar a un robot en su entorno de trabajo:**
   - **Abastecimiento energético**: Dependencia de baterías y autonomía limitada (Ejemplo: robot Andromina OFF ROAD).
   - **Gestión de carga/descarga de baterías**: Necesidad de sistemas de carga autónoma.
   - **Cargas e inercias**: Desestabilización al manipular objetos pesados (Ejemplo: robot Scara SR-20iA).
   - **Selección del tipo de robot**: Elección incorrecta afecta eficiencia y costos (Ejemplo: robots Delta para empaquetado).
   - **Complejidad y adaptación**: Dificultad para reconfigurar robots en entornos cambiantes.
   - **Ruteado de cables/tuberías**: Interferencias y mantenimiento complicado.
   - **Planificación del movimiento**: Optimización de trayectorias y evasión de obstáculos.
   - **Ubicación y SLAM**: Navegación en entornos desconocidos.

---

3. **Comparación entre programación manual (Teach Pendant) y automática (estructurada):**
   |  **Característica**      | **Programación Manual (Teach Pendant)**          | **Programación Automática (Estructurada)**       |
   |--------------------------|--------------------------------------------------|--------------------------------------------------|
   | **Facilidad de uso**     | Alta (intuitivo, sin código)                     | Media-Baja (requiere conocimientos avanzados)    |
   | **Flexibilidad**         | Limitada a tareas repetitivas                    | Alta (adaptable a cambios y sistemas complejos)  |
   | **Precisión**            | Depende del operador                             | Alta (optimizable en simulación)                 |
   | **Aplicaciones típicas** | Soldadura, pintura, ensamblaje simple            | Automatización avanzada, logística, IA           |
   - **Situaciones preferidas**:
     - **Teach Pendant**: Tareas repetitivas y simples (ej. líneas de producción).
     - **Programación estructurada**: Procesos complejos con integración de sensores o IA (ej. robots colaborativos o humanoides).

---

4. **Control por realimentación de posición vs. control por par dinámico:**
   - **Control por posición**: Ajusta los ángulos de las articulaciones para alcanzar una posición final deseada. (ej. robots de ensamblaje industrial).
   - **Control por par dinámico**: Este control regula fuerzas/torques en las articulaciones, mientras que el control cinemático (posición/velocidad) se enfoca en movimientos sin considerar fuerzas.

---

5. **Ventajas y desventajas del uso de IA en robots autónomos:**
   - **Ventajas**:
     - Optimización de movimientos mediante redes neuronales o aprendizaje por refuerzo.
     - Adaptabilidad a entornos dinámicos (ej. robots humanoides).
   - **Desventajas**:
     - Complejidad técnica y necesidad de grandes cantidades de datos.
     - Riesgos éticos: desplazamiento de empleos, decisiones autónomas en contextos críticos.

---

6. **Importancia de la seguridad en sistemas robotizados y normativas relevantes:**
   - **Importancia**: Previene accidentes en interacciones humano-robot mediante sensores de proximidad, sistemas de emergencia y cumplimiento de normativas.
   - **Normativas**:
     - **ISO 10218-1**: Seguridad en robots industriales.
     - **ANSI/RIA R15.06**: Estándares para integración segura de robots.

## Main.py

### urls de ejemplo
https://www.youtube.com/watch?v=ABFqbY_rmEk
https://www.youtube.com/watch?v=sa8Drcbseg0

### requisitos
ffmeg ha de ser instalado en el sistema
    - `ffmeg` (https://www.youtube.com/watch?v=JR36oH35Fgg)
    - `yt-dlp`
    - `openai-whisper`
    - `nltk`
    - `sumy`

### notas
no funciona correctamente en español, transcripciones más lentas y de mucha peor calidad
los modelos tiny, medium, large tienen una gran diferencia de velocidad entre estas.
todo el mundo usa ffmeg para convertir audio