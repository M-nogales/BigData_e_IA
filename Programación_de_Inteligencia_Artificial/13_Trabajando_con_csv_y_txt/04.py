'''EJERCICIO 04
El fichero calificaciones.csv contiene las calificaciones de un curso. Durante el curso se
realizaron dos exámenes parciales de teoría y un examen de prácticas. Los alumnos que tuvieron
menos de 4 en alguno de estos exámenes pudieron repetirlo en al final del curso (convocatoria
ordinaria). Escribir un programa que contenga las siguientes funciones:

1. Una función que reciba el fichero de calificaciones y devuelva una lista de diccionarios,
donde cada diccionario contiene la información de los exámenes y la asistencia de un
alumno. La lista tiene que estar ordenada por apellidos.

2. Una función que reciba una lista de diccionarios como la que devuelve la función
anterior y añada a cada diccionario un nuevo par con la nota final del curso. El peso de
cada parcial de teoría en la nota final es de un 30% mientras que el peso del examen de
prácticas es de un 40%.

3. Una función que reciba una lista de diccionarios como la que devuelve la función
anterior y devuelva dos listas, una con los alumnos aprobados y otra con los alumnos
suspensos. Para aprobar el curso, la asistencia tiene que ser mayor o igual que el 75%,
la nota de los exámenes parciales y de prácticas mayor o igual que 4 y la nota final mayor
o igual que 5.
'''

def dictionary_assist_exams_apells (folder):
    dictionary = []

    with open(folder, "r", encoding="utf-8") as f:
        lines = f.readlines()
        keys = lines[0].strip().split(";")

        for line in lines[1:]:
            values = line.strip().split(";")
            # zip(keys, values) devuelve una tupla con keys y values
            dictionary.append(dict(zip(keys, values)))

    return sorted(dictionary, key=lambda x: x["Apellidos"])

def final_notes(dictionary):
    for student in dictionary:
        attendance = float(student["Asistencia"].replace("%", ""))*0.3
        
        if not student["Ordinario1"] or not student["Ordinario2"]:
            teorical = (float(student["Parcial1"].replace(",",".")) + float(student["Parcial2"].replace(",",".")))/2*0.3

        if student["Ordinario1"] and not student["Ordinario2"]:
            teorical = float(student["Ordinario1"].replace(",","."))*0.3

        if student["Ordinario2"]:
            teorical = float(student["Ordinario2"].replace(",","."))*0.3

        if student["OrdinarioPracticas"]:
            practices = float(student["OrdinarioPracticas"].replace(",","."))*0.4
        elif student["Practicas"]:
            practices = float(student["Practicas"].replace(",","."))*0.4
        else:
            practices = 0
        #? entiendo que si no tienes las practicas hechas se supenden pero puedes aprobar
        #? if practices == 0: student["Nota final"] = 0
        student["Nota final"] = attendance + teorical + practices
    return dictionary

def students_approved_suspended(dictionary):
    approved = []
    suspended = []
    #supongo que no se tiene en cuenta las ordinarias
    for student in dictionary:
        if student["Nota final"] >= 5 and float(student["Asistencia"].replace("%", "")) >= 75 and float(student["Parcial1"].replace(",",".")) >= 4 and float(student["Parcial2"].replace(",",".")) >= 4 and student["Practicas"] and float(student["Practicas"].replace(",",".")) >= 4:
            approved.append(student)
        else:
            suspended.append(student)
    return approved, suspended

#print('dictionary_assist_exams_apells("data/calificaciones.csv"): ', dictionary_assist_exams_apells("data/calificaciones.csv"))
#print('final_notes(dictionary_assist_exams_apells("data/calificaciones.csv")): ', final_notes(dictionary_assist_exams_apells("data/calificaciones.csv")))

approved, suspended =  students_approved_suspended(final_notes(dictionary_assist_exams_apells("data/calificaciones.csv")))

print("Aprobados:")
for a in approved:
    print(a["Nombre"])

print("\nSuspendidos:")
for s in suspended:
    print(s["Nombre"])