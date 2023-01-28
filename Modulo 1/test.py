
with open("database.txt","r") as file:
        city = file.readlines()
file.close()

ciudades = []

for i in range(len(city)):
    city[i] = city[i].replace("\n","")
    ciudades.append(city[i].split(","))

ciudades.pop(0)

print(ciudades)
