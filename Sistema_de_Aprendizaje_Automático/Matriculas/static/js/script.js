const dropZone = document.getElementById('drop-zone');
const fileInput = document.getElementById('license-image');
const fileName = document.getElementById('file-name');
const preview = document.getElementById('preview');
const licenseText = document.getElementById('license-text');
const loader = document.getElementById('loader');
const errorMessage = document.getElementById('error-message');
const submitButton = document.getElementById('submit-btn');
const submitText = document.getElementById('submit-text');

// Función para manejar la selección o arrastre de archivo
function handleFile(file) {
    if (file) {
        // Validar formato de imagen
        const validFormats = ['image/jpeg', 'image/png'];
        if (!validFormats.includes(file.type)) {
            errorMessage.classList.remove('hidden');
            return;
        }
        errorMessage.classList.add('hidden');
        fileName.textContent = file.name;
        
        // Crear una previsualización de la imagen
        const reader = new FileReader();
        reader.onload = function(e) {
            preview.innerHTML = `<img src="${e.target.result}" class="h-full w-full object-contain" alt="Previsualización de la matrícula">`;
        }
        reader.readAsDataURL(file);
    }
}

// Evento para selección de archivo
fileInput.addEventListener('change', function(e) {
    handleFile(e.target.files[0]);
});

// Eventos para arrastrar y soltar
dropZone.addEventListener('dragover', function(e) {
    e.preventDefault();
    dropZone.classList.add('bg-blue-700');
});

dropZone.addEventListener('dragleave', function(e) {
    e.preventDefault();
    dropZone.classList.remove('bg-blue-700');
});

dropZone.addEventListener('drop', function(e) {
    e.preventDefault();
    dropZone.classList.remove('bg-blue-700');
    handleFile(e.dataTransfer.files[0]);
});

// Enviar la imagen al backend y manejar la respuesta
const form = document.querySelector('form');
form.addEventListener('submit', function(event) {
    event.preventDefault();
    loader.classList.remove('hidden');
    errorMessage.classList.add('hidden');
    submitText.classList.add('hidden'); // Ocultar el texto "Procesar imagen"
    preview.innerHTML = ''; // Limpiar cualquier imagen previa

    const formData = new FormData();
    const file = fileInput.files[0];
    formData.append('license-image', file);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        loader.classList.add('hidden'); // Ocultar el loader
        submitText.classList.remove('hidden'); // Mostrar nuevamente el texto "Procesar imagen"

        if (data.image) {
            // Mostrar la imagen procesada solo si la matrícula fue detectada
            const img = new Image();
            img.src = 'data:image/jpeg;base64,' + data.image;
            img.classList.add('h-full', 'w-full', 'object-contain');
            preview.innerHTML = '';
            preview.appendChild(img);
        } else {
            preview.innerHTML = ''; // No mostrar imagen si no se encontró matrícula
        }

        if (data.text) {
            // Mostrar el texto reconocido en mayúsculas
            licenseText.textContent = data.text.toUpperCase();
        } else {
            // Si no se reconoce texto, limpiar el área
            licenseText.textContent = 'No se pudo reconocer la matrícula.';
        }
    })
    .catch(error => {
        loader.classList.add('hidden'); // Ocultar el loader
        errorMessage.classList.remove('hidden'); // Mostrar el mensaje de error
        errorMessage.style.color = 'red'; // Asegurar que el error sea rojo
        console.error('Error:', error);
    });
});
