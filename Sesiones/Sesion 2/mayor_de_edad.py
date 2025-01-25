#solicita al usuario que ingrese su edad
edad=int(input("Ingrese su edad: "))

if edad > 18:
    print(f"Tu edad: {edad}, nos indicaa que eres mayor de edad")
else:
    print(f"Tu edad: {edad}, nos indica que eres menor de edad")