# Monitorización de Aplicaciones con Prometheus y Grafana

## Objetivos
Al finalizar esta práctica, el alumnado será capaz de:
* Instalar y ejecutar Prometheus y Grafana utilizando Docker y Docker Compose, así como Portainer.io.
* Exponer métricas desde un servicio Node.js mediante `prom-client`.
* Configurar Prometheus para recolectar métricas personalizadas.
* Visualizar y analizar métricas en tiempo real desde Grafana.
* Diseñar dashboards con visualizaciones clave de rendimiento.
* Comprender conceptos clave como `scrape interval`, `histogramas`, `counters`, y `gauges`.

## Requisitos previos
* Tener instalado Docker y Docker Compose.
* Conocimientos básicos de Node.js y Express.
* Conocimientos básicos de HTTP (verbos, respuestas, rutas).
* Editor de texto y terminal de comandos.

## Ejercicio 1: Preparar el entorno de monitorización

### Ejercicio 1.1 – Crea un archivo `docker-compose.yml` que levante los servicios `grafana` y `prometheus` en red local, mapeando sus puertos (Grafana: 3000, Prometheus: 9090).

### Ejercicio 1.2 – Crea un archivo `prometheus.yml` que defina dos jobs: `prometheus_service` y `nodejs_service`, escuchando en los puertos adecuados.
💡 **Consejo:** Usa `host.docker.internal` como IP si estás en Windows o Mac.

## Ejercicio 2: Crear un microservicio con métricas

### Ejercicio 2.1 – Desarrolla un servicio mínimo en Node.js que use `express` y exponga al menos una ruta GET `/cities`.

### Ejercicio 2.2 – Instala `prom-client` y añade un archivo `metrics.js` donde definas:
* Un `Counter` de peticiones
* Un `Histogram` de duración
* Un `Gauge` de peticiones en vuelo

### Ejercicio 2.3 – Implementa el endpoint `/metrics` para exponer las métricas recolectadas.
Verifica que accediendo a `http://localhost:3001/metrics` se muestran correctamente las métricas en texto plano.

## Ejercicio 3: Configurar Prometheus y validar la recogida

### Ejercicio 3.1 – Accede a Prometheus en `http://localhost:9090` y comprueba que el job `nodejs_service` aparece como `UP` en Status -> Targets.

### Ejercicio 3.2 – Ejecuta algunas llamadas manuales a tu API (`/cities`) y luego verifica que las métricas como `http_requests_total` aumentan en Prometheus.

## Ejercicio 4: Crear dashboards en Grafana

### Ejercicio 4.1 – Accede a `http://localhost:3000`, cambia la contraseña del usuario `admin`, y añade Prometheus como data source.

### Ejercicio 4.2 – Crea un nuevo dashboard llamado **Monitorización Node.js**.
Añade paneles con las siguientes visualizaciones:
* Número total de peticiones (`http_requests_total`)
* Tiempo medio de respuesta (`http_request_duration_seconds`)
* Peticiones en vuelo (`http_requests_in_flight`)
* Distribución por códigos de estado

### Ejercicio 4.3 – Realiza pruebas de carga simuladas (con `curl` o Postman) y observa la variación de las métricas en tiempo real.

## Ejercicio 5

* ¿Cuál es la diferencia entre un `Counter` y un `Gauge`?
* ¿Por qué Prometheus hace scraping en lugar de usar push?
* ¿Qué ventaja tiene usar `Histogram` frente a un simple `Gauge` para medir latencias?
* ¿Qué problemas podrían surgir si usas muchas etiquetas dinámicas (por ejemplo, user ID)?

## Estructura del Proyecto Final
Sube a tu repositorio y haz un Blackboard un ZIP con la siguiente estructura:



monitoring\_project/
├── docker-compose.yml
├── prometheus.yml
├── grafana\_data/         (si se desea exportar dashboards)
├── src/
│   ├── app.js
│   └── metrics.js
├── README.md             (breve explicación del proyecto)
└── dashboard\_export.json (opcional)



## Bibliografía

* [Documentación oficial de Prometheus](https://prometheus.io/docs/)
* [Prom-client para Node.js](https://github.com/siimon/prom-client)
* [Documentación de Grafana](https://grafana.com/docs/)
* [Curso gratuito: Monitoring with Prometheus and Grafana](https://grafana.com/academy/courses/monitoring-with-prometheus-and-grafana/)
* [Libro: Prometheus: Up & Running – Brian Brazil. O’Reilly Media, 2020.](https://www.oreilly.com/library/view/prometheus/9781492094320/)
