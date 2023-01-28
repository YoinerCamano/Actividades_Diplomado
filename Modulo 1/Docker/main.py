from fastapi import FastAPI

app = FastAPI()

ciudades = []                                   #lista para añadir los datos del archivo database.tx

with open("database.txt", "r") as file:
    city = file.readlines()
file.close()

for i in range(len(city)):
    city[i] = city[i].replace("\n","")          # se eliminan los saltos de la lista 
    ciudades.append(city[i].split(","))         # se reemplaza la lista city por ciudades y se separa sus items por comas(,)

@app.get("/Status")             #endpoint para dar como activo el API
def health():                                  
    return{
        "status": 200,
        "description" : "API Activo"
    }

@app.get("/Cities")             #endpoint para mostrar las ciudades de los paises                
def cities():
    ciudad = ""                                 
    try:
        for i in range(len(ciudades)):              
            ciudad += ciudades[i][1] + ","          #se recorre la lista ciudades y sacamos las ciudades de la misma, pero como un string separado por coma
        description = "Capital de los Paises"
        status = 200
    except:
        status = 400
        description = "Error 400"
        ciudad = "none"

    return{
        "Status": status,
        "ciudades": ciudad,
        "Description": description
    }

@app.post("/Input City")        #endpoint donde con la ciudad se devuelve el pais 
def param(input_city: str):
    country = ""
    input_city = input_city.rstrip()       #se eliminan los posibles espacios en blanco del final del string 
    input_city = input_city.lstrip()       #se eliminan los posibles espacios en blanco del principio del string
    input_city = input_city.lower()        #se convierte toda la entrada en minuscula 

    try:
        for i in range(len(ciudades)):          
            temp = ciudades[i][2].lstrip()      #se elimina los espacios en blanco del principio del string y los asignamos en una variable temporal.
            temp = temp.lower()                 #se convierte el string en minuscula, y se la asignamos a la misma variable temporal.
            if temp == input_city:              #se busca las coincidencias de la ciudad
                country = ciudades[i][1]            #se extrae el pais de la ciudad
                description = "Pais de la ciudad"

        if country == "":                       #caso en el que la varaible tiene un string vacio, por tanto no hubo coincidencia alguna. 
            country = "none"
            description = "¡La ciudad no exite!"

        status = 200
        
    except:
        status = 400
        description = "Error 400"
        country = "none"

    return{
        "Status": status,
        "Pais": country,
        "Description": description

    }

@app.post("/Input ID")         #endpoint donde con el id se devuelve el pais y ciudad
def param(input_ID: int):
    country_out = ""

    try:
        for i in range(len(ciudades)):
            temp = int(ciudades[i][0])                                           #convertimos el id de la lista en un entero 
            if temp == input_ID:                                                 #comparamos el id entrante con el id de la lista en la posicion actual 
                country_out = ciudades[i][1]                                    #se extrae con el id coincidente el pais y la ciudad para pasarlo a un string
                city_out = ciudades[i][2]
                description = "Pais y ciudad del ID"  
        if country_out == "":                                                   #caso en el que la varaible tiene un string vacio, por tanto no hubo coincidencia alguna.
            description = "¡El ID no existe!"
            country_out = "none"
            city_out = "none"

        status = 200              
    
    except:
        status = 400
        description = "Error 400"
        country_out = "none"

    return{
        "Status": status,
        "Pais": country_out, "Ciudad": city_out,
        "Description" : description   

    }

@app.post("/City Add")          #endpoint para agragar un pais y una ciudad     
def add_city(input_country: str, city_add: str):
    try:
        id = len(ciudades) - 1                  #se hace para conocer el tamaño de la lista de ciudades, se le recta -1 para dar la posicion del ultimo id 
        id = int(ciudades[id][0]) + 1           #se toma la el ultimo id, se pasa a entero y se le sumamos 1, 
        
        input_country = input_country.rstrip()          #se eliminan posibles espacios en blanco al final del string
        input_country = input_country.lstrip()          #se eliminan posibles espacios en blanco al principio del string   
        input_country = input_country.lower()           #se convierte el string en minuscula 

        city_add = city_add.rstrip()                   #se eliminan posibles espacios en blanco al final del string        
        city_add = city_add.lstrip()                     #se eliminan posibles espacios en blanco al principio del string
        city_add = city_add.lower()                       #se convierte el string en minuscula

        input_country = " " + input_country             #se agrega un espacio al principio para tener armonia con el resto de la lista
        city_add = " " + city_add                          

        ciudades.append([str(id),input_country, city_add])           #se agrega la nueva ciudad con id, pais y ciudad a la lista de ciudades
    
        with open("database.txt", "w") as file:                 #se abre el archivo database en modo escritura para implementar los cambios           
            for x in ciudades:                                  #se extrae el id, pais y ciudad  de la lista ciudades y las almacenamos en una variable temporal equis x
                y = ""                                          #se declara una variable temporal y donde almacenaremos el id, pais y ciudad como un string separado por coma
                for i in range(3):                              #se interactua en x el pais, ciudad e id para convertir a string separado por comas al principio, sin poner coma al final como el archivo original
                    if i< 2 :
                        y += str(x[i]) + ","
                    else: 
                        y += str(x[i])
                file.write(str(y) + "\n")                       #se pasa ese el string de la variable temporal y con salto de linea
        file.close()
        status = 200
        description = "Pais y ciudad Agregados correctamente"
    except:
        status = 400
        input_country = "none"
        city_add = "none"
        description = "error 400"


    return{
        "Status": status,
        "Id Asignado": str(id),
        "Pais Agregado": input_country,
        "Ciudad Agregada": city_add,
        "Description": description
    }

@app.get("/City Remove")       #endpoint para remover pais y ciudad con el id 
def remove(ID : int):
    try:
        for i in range(len(ciudades)):     
            temp = int(ciudades[i][0])                  #se saca el id de la lista de ciudades, se pasa a entero y lo almanecamos en una variable temporal 
            if temp == ID:                               #se busca la coincidencia del id sumistrado con los id's de las ciudades. 
                country_remove = ciudades[i][1]           # se guarda ciudad y pais para mostrar en la API pais y ciudad eliminados
                city_remove = ciudades[i][2]
                ciudades.pop(i)                         # se elimina la el id, ciudad y pais si se encuentra la coicidencia.
                description = "Eliminado Correctamente"
            else:
                description = "ID no encontrado"    #si no hay ninguna coicidencia
                country_remove = "None" 
                city_remove = "None"

        with open("database.txt", "w") as file:    #se abre el database en modo escritura para guardar las modificaciones 
            for x in ciudades:                     # se interactua las ciudades, y se almacenan en una varaible temporal x; se hace lo mismo que en anterior endpoint (City Add)
                y = ""
                for i in range(3):                  
                    if i< 2 :
                        y += str(x[i]) + ","
                    else: 
                        y += str(x[i])
                file.write(str(y) + "\n")
            file.close()

        status = 200

    except:
        status = 400
        description = "Error 400"
        country_remove = "None" 
        city_remove = "None"

    return{
        "Status": status,
        "Pais Removido": country_remove,
        "Ciudad Removida": city_remove,
        "Description": description
    }