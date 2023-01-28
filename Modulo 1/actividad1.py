"""
Dada la siguiente lista de estudiantes, cree un script usando ciclos, condiciones, variables y si quiere, funciones, que almacene los valores en las siguientes variables:

 promedio_edad -> el promedio de las edades de los estudiantes.
 num_menores_edad -> el numero de estudiantes menores de edad.
 num_mayores_edad -> el numero de estudiantes mayores de edad.
 porcentaje_mujeres -> el porcentaje de mujeres en el grupo.
 porcentaje_hombres -> el porcentaje de hombres en el grupo.
 estudiantes_activos -> numero de estudiantes activos.
"""

my_students = [
    {
        "nombre": "Juan",
        "edad": 23,
        "genero": "M",
        "activo": False
    },
    {
        "nombre": "Maria",
        "edad": 25,
        "genero": "F",
        "activo": True
    },
    {
        "nombre": "Lucia",
        "edad": 35,
        "genero": "F",
        "activo": False
    },
    {
        "nombre": "Pedro",
        "edad": 30,
        "genero": "M",
        "activo": True
    },
    {
        "nombre": "Luis",
        "edad": 15,
        "genero": "M",
        "activo": True
    }
]

edad= 0
student_min = 0
estudiantes_activos = 0
cant_hombres = 0

cant_students = len(my_students) #cantidad de estudiantes. 

for i in range(cant_students):

    edad += (my_students[i]['edad']) #sumatoria de edades de los estudiantes. 
    
    if my_students[i]['edad'] < 18: # sumatoria de edades en estudiantes menores de edad, teniedo este dato sabemos los estudiantes mayores de edad.  
        student_min += 1

    if my_students[i]['activo'] == True : 
        estudiantes_activos += 1

    if my_students[i]['genero'] == 'M':   #condicion para saber la cantidad de hombres activos, tiendo este dato podemos saber cuantas mujeres hay 
        cant_hombres += 1

promedio_edad = edad/cant_students
num_menores_edad = student_min
num_mayores_edad = cant_students - student_min
porcentaje_hombres = (cant_hombres/cant_students)*100
porcentaje_mujeres = ((cant_students-cant_hombres)/cant_students)*100

print("El promedio de las edades entre los estudiantes es",promedio_edad)
print("Estudiantes Menores de edad",num_menores_edad)
print("Estudiantes Mayores de edad",num_mayores_edad)
print("Porcentaje de Hombres en el grupo",porcentaje_hombres,"%")
print("Porcentaje de Mujeres en el grupo",porcentaje_mujeres,"%")
print("Estudiantes Activos",estudiantes_activos)
    