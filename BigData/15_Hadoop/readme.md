error fixes

docker-compose -p hadoop up -d
docker exec -it hadoop-namenode-1 /bin/bash ||| docker exec -it hadoop-namenode-1 sh

Cómo usar vi para editar:
Presiona i para entrar en modo de inserción y editar el archivo.
Edita el contenido según lo necesites.
Para salir:
Presiona Esc, escribe :wq y presiona Enter para guardar y salir.
Si quieres salir sin guardar, usa :q! y presiona Enter.

docker exec -it hadoop-namenode-1 sh
cd share/hadoop/mapreduce/ #accedemos a la carpeta map-reduce del entorno
ls #mostramos los archivos disponibles
yarn jar hadoop-mapreduce-examples-3.3.6.jar pi 10 15 
#utilizamos yarn en la ejecucion de los ejemplos par aprobar el funcionamiento de map-reduce




hdfs dfs -mkdir -p /user/bigdata/input #creamos una carpeta en hdfs 
#(si no la hemos creado ya)
cd /tmp #abrimos la carpeta tmp
#en otra consola con acceso a nuestro sistema ráiz 
#utilizamos docker para copiar el archivo al contenedor
docker cp elQuijote.text nombreDelContendor:/tmp
#volvemos a la consola del contenedor
ls #comprobamos que esté el archivo dentro de tmp
hdfs dfs -put elQuijote.txt /user/bigdata/input #añadimos elQuijote al sistema de archivo hdfs
hdfs dfs -ls /user/bigdata/input #comprobamos que está dentro
#luego navegamos a 
cd ~/share/hadoop/mapreduce
#puede ser necesario ampliar el uso de memoria de forma ilimitada:
ulimit -c unlimited
# por último, ejecutamos el cálculo aplicado en la carpeta de entrada
# y le asignamos una carpeta de salida
yarn jar hadoop-mapreduce-examples-3.3.6.jar wordcount /user/bigdata/input /user/bigdata/output

hdfs dfs -cat /user/bigdata/output/part-r-00000


hdfs dfs -mkdir -p /user/bigdata/datos
hdfs dfsadmin -allowSnapshot /user/bigdata/datos
hdfs dfs -createSnapshot /user/bigdata/datos snapshot1