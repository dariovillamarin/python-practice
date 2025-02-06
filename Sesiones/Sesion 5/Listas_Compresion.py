# Listas por compresión

# Sintaxis: expresion for item in iteracción if condición

# Ejemplo 1 Lista de numeros pares del 1 al 9

numeros_pares= [x for x in range(10) if x % 2 ==0]
print(numeros_pares)

# Ejemplo 2: Crear una lista con los cuadrados de los números del 1 al 5

cuadrados=[x**2 for x in range(1,6)]
print(cuadrados)

# Eejemplo 3: Crea una lista que contenga los números impares del 1 al 20.

numeros_impares=[x for x in range(20) if x % 2 != 0]
print(numeros_impares)