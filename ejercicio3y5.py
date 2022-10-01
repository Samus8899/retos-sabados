convertir = lambda nombre,edad, ocupacion : {"nombre":nombre,"edad":edad,"ocupacion":ocupacion}

nombre = input("escriba el nombre: ")
edad = input("escriba la edad: ")
ocupacion= input("escriba la ocupacion: ")

print(convertir(nombre,edad,ocupacion))

numero = int(input("ingrese el numero: "))
multiplicar = lambda numero : numero*100

print(multiplicar(numero))
