// Inicializar el grafo Cytoscape
let cy = cytoscape({
  container: document.getElementById('cy'), // El div donde se renderiza el grafo
  elements: [], // Inicialmente vacío
  style: [
      {
          selector: 'node',
          style: {
              'background-color': '#6366f1',
              'label': 'data(id)'
          }
      },
      {
          selector: 'edge',
          style: {
              'width': 2,
              'line-color': '#ccc',
              'target-arrow-color': '#ccc',
              'target-arrow-shape': 'triangle', // Flecha al final para indicar dirección
              'curve-style': 'bezier', // Curva para mayor claridad
              'arrow-scale': 1.5, // Tamaño de la flecha
              'label': 'data(weight)', // Mostrar el peso en la arista
              'text-rotation': 'autorotate', // El texto rota con la línea
              'font-size': 12,
              'text-margin-y': -10
          }
      }
  ],
  layout: {
      name: 'grid',
      rows: 3
  }
});

// Función para añadir un nodo
function addNode() {
  const nodeId = document.getElementById('nodeId').value.toUpperCase();
  if (nodeId) {
      cy.add({
          data: { id: nodeId }
      });
      cy.layout({ name: 'grid', rows: 3 }).run(); // Reorganizar layout
      document.getElementById('nodeId').value = ''; // Limpiar campo
  } else {
      alert("Por favor ingrese un ID de nodo válido.");
  }
}

// Función para añadir una arista
function addEdge() {
  const source = document.getElementById('source').value;
  const target = document.getElementById('target').value;
  const weight = document.getElementById('weight').value;

  if (source && target && weight) {
      cy.add({
          data: { source: source, target: target, weight: weight }
      });
      cy.layout({ name: 'grid', rows: 3 }).run(); // Reorganizar layout
      document.getElementById('source').value = ''; // Limpiar campos
      document.getElementById('target').value = '';
      document.getElementById('weight').value = '';
  } else {
      alert("Por favor ingrese el nodo origen, destino y el peso.");
  }
}

// Función para resetear el grafo
function resetGraph() {
  cy.elements().remove(); // Elimina todos los elementos del grafo
}

// Función para alternar la dirección (flechas) en las aristas
function toggleDirection() {
  const showArrows = document.getElementById('directedCheckbox').checked;
  
  cy.style().selector('edge').style({
      'target-arrow-shape': showArrows ? 'triangle' : 'none' // Mostrar o no las flechas
  }).update(); // Actualizar el estilo de las aristas
}
