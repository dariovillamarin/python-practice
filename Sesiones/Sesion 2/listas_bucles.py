#ejercicio de listas y bucles
lstNumeros=[1,2,3,4,5]

#impresión de los números

print("La lista tiene estos números \n ")
for numero in lstNumeros:
    print(numero)


print("\nUsando bucle while para números pares:")
contador = 0
while contador < len(lstNumeros):
    if(lstNumeros[contador] % 2 ==0):
        print(lstNumeros[contador])
    contador +=1

