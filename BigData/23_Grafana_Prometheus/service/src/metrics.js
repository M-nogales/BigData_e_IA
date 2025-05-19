const client = require('prom-client');

// Colección de métricas por default (CPU, GC, memoria, etc.)
client.collectDefaultMetrics();

// Counter
const requestCounter = new client.Counter({
  name: 'http_requests_total',
  help: 'Número total de peticiones HTTP',
});

// Histogram
const requestHistogram = new client.Histogram({
  name: 'http_request_duration_seconds',
  help: 'Duración de las peticiones HTTP en segundos',
  buckets: [0.1, 0.3, 0.5, 1, 1.5, 2]
});

// Gauge
const inFlightGauge = new client.Gauge({
  name: 'in_flight_requests',
  help: 'Número de peticiones en curso',
});

// Función para exponer las métricas
const metricsEndpoint = async (req, res) => {
  res.set('Content-Type', client.register.contentType);
  res.end(await client.register.metrics());
};

module.exports = {
  requestCounter,
  requestHistogram,
  inFlightGauge,
  metricsEndpoint
};
