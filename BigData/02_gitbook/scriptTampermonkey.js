// ==UserScript==
// @name         Eliminar Div
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Eliminar un div específico en la página
// @author       Tú
// @match        https://app.gitbook.com/*
// @grant        none
// ==/UserScript==

(function() {
  'use strict';
  // Ejecutar el script repetidamente hasta encontrar el div
  const interval = setInterval(() => {
      const div = document.querySelector('div[style="backdrop-filter: blur(5px);"]');
      if (div) {
          div.remove();
          clearInterval(interval); // Detener la comprobación una vez que el div se haya eliminado
      }
  }, 500); // Comprobar cada 500ms
})();
