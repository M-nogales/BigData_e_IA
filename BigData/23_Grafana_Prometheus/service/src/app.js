const express = require('express');
const app = express();
const port = 3001;

const { requestCounter, requestHistogram, inFlightGauge, metricsEndpoint } = require('./metrics');

// Middleware para métricas
app.use((req, res, next) => {
  inFlightGauge.inc();
  const end = requestHistogram.startTimer();
  requestCounter.inc();

  res.on('finish', () => {
    inFlightGauge.dec();
    end(); // Finaliza el histograma
  });

  next();
});

// Ruta principal
app.get('/cities', (req, res) => {
  res.json(['Madrid', 'Barcelona', 'Valencia']);
});

// Endpoint de métricas
app.get('/metrics', metricsEndpoint);

// Start server
app.listen(port, () => {
  console.log(`Servidor escuchando en http://localhost:${port}`);
});
