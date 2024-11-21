# 02. **Calificaciones de Estudiantes**
''' Pide al usuario que ingrese las calificaciones de 10 estudiantes.
Crea una Serie con las calificaciones y asigna nombres de estudiantes como índice.
Calcula el promedio, la mediana y la desviación estándar de las calificaciones.
Reemplaza las calificaciones que están por debajo de 50 con "Reprobado".
Muestra los estudiantes con calificaciones aprobatorias.
 '''
import pandas as pd

while True:
    try:
        notes = [int(input(f'Dime la calificación del estudiante {i+1}: ')) for i in range(10)]
        break
    except ValueError:
        print('Solo se permiten números enteros')

students = ['Student 1', 'Student 2', 'Student 3', 'Student 4', 'Student 5', 'Student 6', 'Student 7', 'Student 8', 'Student 9', 'Student 10']
notes = pd.Series(notes, index=students, dtype='object')
print('notes: ', notes)
print('Promedio: ', notes.mean())
print('Mediana: ', notes.median())
print('Desviación estándar: ', notes.astype(float).std())
notes[notes.astype(float) < 50] = 'Suspendido'
print('Estudiantes aprobados:\n', notes[notes != 'Suspendido'])