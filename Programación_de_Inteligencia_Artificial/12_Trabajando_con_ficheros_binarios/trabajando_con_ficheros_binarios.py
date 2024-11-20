'''
Desarrollar una clase Empresa cuyos datos miembros sean un nombre, un tamaño máximo
y una lista de empleados. El tamaño de la empresa es inmutable.
Para esta clase se piden los siguientes constructores y métodos:
1. Constructor __init__: recibe como argumentos una cadena de texto 'nombre' y un valor
entero 'tamaño', y construye un nuevo objeto de la clase Empresa.
 La lista de empleados debe tener una longitud limitada por el valor de 'tamaño'.

2. Métodos de acceso get_nombre y get_tamaño: devuelven el nombre y el tamaño de la
empresa, respectivamente.
3. Método get_empleado: recibe como argumento un índice entero menor que el tamaño de
la empresa, y devuelve el empleado en esa posición de la lista.
4. Método despide_empleado: recibe como argumento un índice entero menor que el
tamaño de la empresa, y asigna 'None' en la posición correspondiente de la lista de
empleados para indicar que el empleado fue despedido.

'''

import struct
from typing import final


class Empresa:
    def __init__(self, nombre, tamaño):
        self.nombre = nombre
        self.tamaño = tamaño
        self.empleados = [None] * tamaño
        self.archivo = 'MisEmpleados.dat'
        self.cargar_empleados()

    def get_nombre(self):
        return self.nombre

    def get_tamaño(self):
        return self.tamaño

    def get_empleado(self, i):
        return self.empleados[i]

    def despide_empleado(self, i):
        if 0 <= i < self.tamaño and self.empleados[i] is not None:
            print(f'{self.empleados[i].get_nombre()} a la calle crack')
            self.empleados[i] = None
            self.guardar_empleados()

    def nuevo_empleado(self, nombre, sueldo):
        empleado = Empleado(self, nombre, sueldo)
        for i in range(self.tamaño):
            if self.empleados[i] is None:
                self.empleados[i] = empleado
                self.guardar_empleados()
                break
        else:
            print("No hay espacio para nuevos empleados.")

    def guardar_empleados(self):
        # Guarda los empleados en un archivo binario usando struct.
        with open(self.archivo, 'wb') as file:
            for empleado in self.empleados:
                if empleado is not None:
                    nombre_bin = empleado.get_nombre().encode('utf-8').ljust(30, b'\x00')  # 30 bytes
                    sueldo = empleado.get_sueldo()  # 4 bytes (float)
                    num_empleado = empleado.get_num_empleado()  # 4 bytes (int)
                    # Aseguramos que el tamaño total es 40 bytes
                    file.write(struct.pack('30s f I', nombre_bin, sueldo, num_empleado))

    def cargar_empleados(self):
        # Carga los empleados desde un archivo binario usando struct.
        try:
            with open(self.archivo, 'rb') as file:
                while chunk := file.read(40):  # 40 bytes por empleado
                    if len(chunk) < 40:
                        print("Advertencia: Datos incompletos detectados. Saltando.")
                        continue
                    nombre_bin, sueldo, num_empleado = struct.unpack('30s f I', chunk)
                    nombre = nombre_bin.decode('utf-8').strip()
                    empleado = Empleado(self, nombre, sueldo, num_empleado=num_empleado)
                    if 0 <= num_empleado < self.tamaño:
                        self.empleados[num_empleado] = empleado
        except FileNotFoundError:
            print(f"Archivo '{self.archivo}' no encontrado. Se creará al guardar empleados.")

'''
Desarrollar una clase Empleado cuyos datos miembros sean nombre, sueldo y número de
empleado. Los datos han de ser protegidos (utilizando un guion bajo al inicio de los
nombres de los atributos). El número de empleado debe ser único y generado
automáticamente para cada empleado nuevo.
Para esta clase, se piden los siguientes constructores y métodos:
1. Constructor __init__: recibe como argumentos una referencia a un objeto Empresa, una
cadena de texto 'nombre' y un valor entero 'sueldo'.
 El número de empleado es único y se genera automáticamente.
2. Métodos de acceso get_nombre, get_sueldo y get_num_empleado: permiten obtener el
nombre, sueldo y número de empleado, respectivamente.
3. Métodos modificadores set_nombre y set_sueldo: permiten modificar el nombre y sueldo
del empleado.
4. Método __str__: devuelve una cadena con el número, nombre y sueldo del empleado.
5. Método aumentar_sueldo: recibe un porcentaje y aumenta el sueldo del empleado en ese
porcentaje. Este método no puede ser sobrescrito por clases
 derivadas (decorador @final en Python 3.8+).
6. Método despedir: elimina al empleado de la empresa y actualiza el archivo de empleados.
'''
#! _num_empleado = 0 y los if en la declaración del constructor son para que el número de empleado sea único y se genere automáticamente.
class Empleado:
    _num_empleado = 0

    def __init__(self, empresa, nombre, sueldo, num_empleado=None):
        self._nombre = nombre
        self._sueldo = sueldo
        if num_empleado is None:
            self._num_empleado = Empleado._num_empleado
            Empleado._num_empleado += 1
        else:
            self._num_empleado = num_empleado
        self.empresa = empresa

    def get_nombre(self):
        return self._nombre

    def get_sueldo(self):
        return self._sueldo

    def get_num_empleado(self):
        return self._num_empleado

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_sueldo(self, sueldo):
        self._sueldo = sueldo

    def __str__(self):
        return f'Empleado {self._num_empleado}: {self._nombre}, sueldo: {self._sueldo}'

    @final
    def aumentar_sueldo(self, porcentaje):
        self._sueldo += self._sueldo * porcentaje / 100

    def despedir(self):
        self.empresa.despide_empleado(self._num_empleado)

'''Agregar un método nuevo_empleado en la clase Empresa, que recibe un nombre y sueldo,
crea un nuevo empleado asociado a la empresa y lo añade a la lista
de empleados. Cada vez que se agrega o elimina un empleado, se debe actualizar el archivo
'MisEmpleados.dat'''


'''
Implementar una clase o función principal que permita realizar las siguientes acciones:
1. Cargar al menos cinco empleados iniciales en la empresa desde el archivo o crear nuevos
si es la primera ejecución.
2. Dar de alta a dos empleados adicionales (utilizando el método nuevo_empleado).
3. Dar de baja a un empleado (utilizando el método despedir).
4. Guardar los cambios en el archivo 'MisEmpleados.dat' después de cada alta o baja de un
empleado.
El archivo 'MisEmpleados.dat' debe almacenar los datos de los empleados, es decir, solo los
datos definidos en la clase Empleado.
'''

# Gestión directa de la empresa y sus empleados
empresa = Empresa("MiEmpresa", 10)

# # Verificar si hay empleados iniciales cargados
print("\nEmpleados iniciales cargados:")
for i in range(empresa.get_tamaño()):
    empleado = empresa.get_empleado(i)
    if empleado:
        print(empleado)

# # Dar de alta dos empleados
print("\nDando de alta a nuevos empleados:")
empresa.nuevo_empleado("Alí", 40000.0)
empresa.nuevo_empleado("Babá", 45000.0)

# # Mostrar empleados
print("\nEmpleados después del alta:")
for i in range(empresa.get_tamaño()):
    empleado = empresa.get_empleado(i)
    if empleado:
        print(empleado)

# # Dar de baja
print("\nDando de baja a un empleado:")
empresa.despide_empleado(0)

# # Mostrar empleados
print("\nEmpleados después de la baja:")
for i in range(empresa.get_tamaño()):
    empleado = empresa.get_empleado(i)
    if empleado:
        print(empleado)
