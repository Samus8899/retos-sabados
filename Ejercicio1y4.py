# 1. funcion lambda que clasifique si un numero es par
numero = int(input("Digite un numero: "))

clasificar = lambda numero: numero%2==0
if(clasificar(numero)):
    print("es multiplo")
else:
    print("no es multiplo")

# 4. Función lambda que sume dos números

numero1= int(input("Digite un numero: "))
numero2= int(input("Digite un numero: "))

sumar = lambda numero1, numero2: numero1+numero2

print(sumar(numero1,numero2))