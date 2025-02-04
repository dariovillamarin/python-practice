# Listas

frutas = ["uva", "sandia", "naranaja", "maracuya"]

print(frutas) # muestra la lista completa
print(frutas[0]) # muestra el primer elemento de la lista

frutas[2]="Mandarina"
print(frutas)

frutas.append("Coco") # añadde un elemento a la lista
print(frutas)

frutas.remove("maracuya") # elimina maracuya de la lista
print(frutas)

for fruta in (frutas): #recorrer una lista
    print (fruta)


# TUPLAS

print("---- TUPLAS ----")

ciudades=("Quito", "Sevilla", "Lisboa")
print(ciudades)
print(ciudades[2])

# CONUNTOS SETS

print("-----CONJUNTOS SETS")

conjunto1={1,2,3,4,5}
conunto2={4,5,6,7,8}

print(conjunto1)
print(conunto2)

print(f"Union: {conjunto1|conunto2}") # Union
print(f"Intersección: {conjunto1 & conunto2}") #intersección


# Diccionarios

libro = {
    "Titulo":"El Monje que vendio su ferrari",
    "Autor":"Robin Sharma",
    "Año" : "2022"

}

print(libro)

libro["Año"]="1980" #modificamos el año
print(libro)

for clave, valor in libro.items():
    print(f"{clave}:{valor}")
