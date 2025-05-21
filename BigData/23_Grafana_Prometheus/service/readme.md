# Monitorización de Aplicaciones con Prometheus y Grafana

Este proyecto tiene como objetivo principal implementar un sistema de monitorización para aplicaciones web usando **Prometheus** y **Grafana**, integrados mediante Docker y Docker Compose.

Se desarrolla un microservicio en **Node.js** que expone métricas personalizadas con la biblioteca `prom-client`. Prometheus se configura para recolectar estas métricas mediante scraping, y Grafana permite visualizar en tiempo real la salud y rendimiento del servicio a través de dashboards interactivos.

El aprendizaje incluye la instalación y configuración de las herramientas, la instrumentación de código para métricas (counters, gauges, histogramas), la creación de queries PromQL para analizar datos y la generación de paneles visuales que facilitan la toma de decisiones y la detección de incidencias.

Con este proyecto, se consolidan conceptos clave en observabilidad moderna, como intervalos de scrape, tipos de métricas, modelos de recolección y buenas prácticas para el etiquetado y escalabilidad del monitoreo.

---

## Algunos conceptos

### 1. ¿Cuál es la diferencia entre un **Counter** y un **Gauge**?

* **Counter**:

  * Es un valor que **solo puede aumentar** (incrementar) o resetearse a cero (por ejemplo, tras reiniciar la aplicación).
  * Se usa para contar eventos acumulativos, como número total de peticiones, errores, etc.
  * Nunca disminuye.

* **Gauge**:

  * Es un valor que puede **subir o bajar** libremente.
  * Representa un estado o cantidad instantánea, por ejemplo, número de peticiones en curso, uso de memoria, temperatura, etc.

---

### 2. ¿Por qué Prometheus hace **scraping** en lugar de usar **push**?

* El modelo de **scraping** (Prometheus va y pregunta a los targets) tiene ventajas:

  * **Control centralizado:** Prometheus controla cuándo y cómo se recogen datos.
  * **Simplicidad:** No necesitas que los servicios implementen un cliente para enviar datos.
  * **Fiabilidad:** Si un servicio está caído, simplemente no responde al scrape; no genera errores de envío ni datos corruptos.
  * **Seguridad y firewall:** Es más fácil controlar accesos, porque el servidor de Prometheus hace las peticiones y no necesitas abrir conexiones salientes en todos los clientes.

---

### 3. ¿Qué ventaja tiene usar **Histogram** frente a un simple **Gauge** para medir latencias?

* El **Histogram**:

  * Recoge **distribuciones** de duración en buckets predefinidos (por ejemplo: <0.1s, <0.3s, etc.).
  * Permite calcular percentiles (p50, p90, p99), visualizar la distribución completa y no solo un valor instantáneo.
  * Se puede usar para estimar la duración promedio, mediana, cola, etc.

* Un simple **Gauge** solo daría el valor actual de latencia en un momento dado, sin contexto histórico ni distribución.

---

### 4. ¿Qué problemas podrían surgir si usas muchas etiquetas dinámicas (por ejemplo, user ID)?

* **Explosión de series temporales:** Cada combinación única de etiquetas genera una serie nueva, y etiquetas muy dinámicas (como user ID) pueden generar miles o millones de series.
* **Alto consumo de memoria y almacenamiento:** Esto puede saturar Prometheus, ralentizar consultas y aumentar costos.
* **Dificultad para agregar o analizar:** Las métricas se vuelven difíciles de agrupar o resumir si hay demasiada granularidad.
* **Riesgo de DoS accidental:** Un atacante o bug puede crear etiquetas arbitrarias y saturar el sistema.