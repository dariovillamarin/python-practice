#ejercicio de funciones, try, except y módulos

import math

def calcular (num1, num2):
    
        #suma
        suma= num1 + num2
        
        #resta
        resta= num1-num2

        #multiplicación
        multiplicacion=num1*num2

        try:
            #división
            division=num1/num2
        except ZeroDivisionError:
            division= "No se puede realizar una división para 0"

        return suma, resta, multiplicacion, division
    

def raiz_cuadrada():
    try:
          numero=float(input("Ingresa un número para calcular raíz cuadrada: "))
          if numero<0:
               print("No se puede calcular la raíz cuadarada de un número negativo")
          else:
               resultado=math.sqrt(numero)
               print(f"La raiza cuadrada de {numero} es {resultado}")

         
    except ValueError:
        print("Ingresae un número válido")

     
    
#solicitar los dos números al usuario
try:
    numero1=int(input("Ingresa el primer número: "))
    numero2=int(input("Ingresa el segundo número: "))

    #llamamos a la función calcular
    suma, resta, multiplicacion, division = calcular(numero1, numero2)

    #mostramos los resultados
    print(f"\n Los resultados con los números {numero1} y {numero2} son:")
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"DivisiónSuma: {division}")

    raiz_cuadrada()
    
except ValueError:
      print("Por favor ingrese un número valido")


