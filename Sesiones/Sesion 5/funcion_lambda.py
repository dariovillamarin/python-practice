# Funciones Lambda

#Las funciones lambda en Python son funciones anónimas (sin nombre) que se definen en una sola línea. 
# Son útiles cuando necesitamos una función pequeña y rápida para pasar como argumento a otras funciones, 
# pero no queremos escribir una definición de función completa usando def.

# sintaxis: lambda argumentos: expresión

# Ejemplo 1, suma de dos números

suma = lambda x,y:x + y
print(suma(3,6))


# Ejemplo 2, ordenar una tupla

tuplas =[(1,3), (2,0), (3,1), (5,2)]

tupla_ordenada=sorted(tuplas, key=lambda x: x[1])

print(tupla_ordenada)

# Ejemplo 3, usando la funcion map()

numeros=[1,2,3,4,5]

cuadrados=list(map(lambda x: x**2,numeros))

print (cuadrados)

# Ejemplo 4, usando la función filter()

numFil=[1,2,3,4,5,6]

pares= list(filter(lambda x:x%2==0,numFil))

print(pares)