from multiprocessing.heap import Arena
from turtle import width


width = int(input("Digite el ancho del rectangulo: "))
height = int(input("Digite la altura del rectangulo: "))

def calcularA(width,height):
    area = width*height
    return area

def calcularP(width,height):
    perimetro = (width*2)+(height*2)
    return perimetro

def pintar(width,height):
    for i in range (height):
        salida=""
        for j in range (width):
            salida = salida + "*"
        print(salida)

print(calcularA(width,height))
print(calcularP(width,height))
pintar(width,height)