### Respuestas a las preguntas:

1. **¿Qué es el hash de un bloque? ¿Por qué es importante que sea único?**  
   El hash de un bloque es un código alfanumérico generado mediante una función criptográfica (en este caso, SHA-256) a partir de la información contenida en el bloque, incluyendo su ID, emisor, receptor, mensaje y el hash del bloque anterior. Es importante que sea único porque garantiza la integridad de la cadena de bloques, evitando modificaciones no autorizadas y asegurando que cada bloque sea identificable de manera exclusiva.

2. **¿Qué ocurre si se modifica un bloque anterior en la cadena?**  
   Si se modifica un bloque anterior, su hash cambiará, lo que a su vez alterará el hash almacenado en el bloque siguiente y así sucesivamente hasta el último bloque. Como resultado, la cadena se volverá inválida, ya que los hashes encadenados ya no coincidirán, detectándose así cualquier intento de manipulación.

3. **¿Qué representa el bloque génesis y qué lo diferencia de los demás?**  
   El bloque génesis es el primer bloque de la cadena y actúa como su punto de inicio. Se diferencia de los demás porque no tiene un hash previo al que enlazarse (su `hash_anterior` suele ser "0" o un valor predefinido). Todos los demás bloques dependen del bloque génesis como base para la continuidad de la cadena.