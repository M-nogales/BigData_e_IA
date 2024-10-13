const NoSQLClient = require("oracle-nosqldb").NoSQLClient;

// Configurar el cliente NoSQL para conectarse a la base de datos
const client = new NoSQLClient({
  serviceType: "KVSTORE", // KVSTORE indica que estamos usando Oracle NoSQL Database en local
  endpoint: "http://localhost:8080", // Dirección del proxy configurado en tu Docker
  // auth: {
  //     Oracle NoSQL Community Edition no requiere autenticación, así que se puede omitir
  // }
});

async function createTable() {
    try {
      const createDDL = `CREATE TABLE IF NOT EXISTS myTable (
        id INTEGER,
        name STRING,
        age INTEGER,
        PRIMARY KEY (id)
      )`;
      const options = {
        tableLimits: {
          readUnits: 50,
          writeUnits: 50,
          storageGB: 25
        }
      };
      //con opciones de configuración
      const res = await client.tableDDL(createDDL, options);
      console.log("Tabla 'myTable' creada. Estado:", res.tableState.name);
  
      // Esperar a que la operación se complete
      await client.forCompletion(res);
      console.log("Tabla 'myTable' está completamente creada.");
    } catch (err) {
      console.error("Error al crear la tabla:", err);
    }
  }

// Función para realizar operaciones básicas, como insertar un registro
async function run() {
  try {
    await createTable();

    // Insertar un registro en una tabla (debes tener la tabla creada)
    const result = await client.put("myTable", {
      id: 1,
      name: "juan",
      age: 616,
    });
    console.log("Registro insertado,juan Mytable:", result);

    // Leer un registro de la tabla
    const getResult = await client.get("myTable", { id: 1 });
    console.log("Registro obtenido,id=1 myTable:", getResult);

    // Consultar registros con edad mayor a 600
    const queryResult = await client.query(
      "SELECT * FROM myTable WHERE age > 600"
    );

    console.log("Registros obtenidos de la consulta,myTable:");
    
    for await (const row of queryResult.rows) {
      console.log(row);
    }
  } catch (err) {
    console.error("Error:", err);
  } finally {
    // Cerrar la conexión con la base de datos
    client.close();
  }
}

async function createKeyValueTable() {
    try {
      const createDDL = `CREATE TABLE IF NOT EXISTS KeyValueTable (
        key STRING,
        value JSON,
        PRIMARY KEY (key)
      )`;
      //sin opciones de configuración
      const res = await client.tableDDL(createDDL);
      console.log("Tabla 'KeyValueTable' creada. Estado:", res.tableState.name);
  
      // Esperar a que la operación se complete
      await client.forCompletion(res);
      console.log("Tabla 'KeyValueTable' está completamente creada.");
    } catch (err) {
      console.error("Error al crear la tabla clave-valor:", err);
    }
  }
  
  async function runKey_Value() {
    try {
      // Crear la tabla para clave-valor
      await createKeyValueTable();
  
      // Inserta un par clave-valor
      const putResult1 = await client.put("KeyValueTable", { key: "myKey1", value: { name: "Juan-valor", age: 33 } });
      console.log("Par clave-valor insertado:", putResult1);
  
      const putResult2 = await client.put("KeyValueTable", { key: "myKey2", value: { name: "Maria-valor", age: 25 } });
      console.log("Par clave-valor insertado:", putResult2);
  
      // Recupera el valor asociado a una clave
      const getResult1 = await client.get("KeyValueTable", { key: "myKey1" });
      console.log("Valor obtenido para myKey1:", getResult1.row);
  
      // Actualiza el valor asociado a una clave
      const updateResult = await client.put("KeyValueTable", { key: "myKey1", value: { name: "Juan-update", age: 31 } }); // Actualizamos la edad
      console.log("Par clave-valor actualizado:", updateResult);
  
      // Recupera el valor actualizado
      const getUpdatedResult = await client.get("KeyValueTable", { key: "myKey1" });
      console.log("Valor actualizado para myKey1:", getUpdatedResult.row);
  
      // Elimina una entrada de la base de datos
      const deleteResult = await client.delete("KeyValueTable", { key: "myKey2" });
      console.log("Entrada eliminada para myKey2:", deleteResult);
  
      // Intenta recuperar el valor eliminado
      const getDeletedResult = await client.get("KeyValueTable", { key: "myKey2" });
      console.log(
        "Valor obtenido para myKey2 (debería ser null):",
        getDeletedResult.row
      );
    } catch (err) {
      console.error("Error:", err);
    } finally {
      // Cerrar la conexión con la base de datos
      client.close();
    }
  }
run();          // Ejecutar operaciones de tabla
runKey_Value(); // Ejecutar operaciones clave-valor