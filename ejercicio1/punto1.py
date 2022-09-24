def implementar():
    vector = []
    for i in range(1,5,1):
        vector.append(int(input(f"Digite el numero de la posicion {i}: ")))
    print(vector)
    return vector

vectorretornado=implementar()

def sumar(vector):
    suma = 0
    for i in range (1,5,1):
        suma = suma + vector[i-1]
    print(suma)
    return suma

resultado = sumar(vectorretornado)

def promediar(suma, vector):
    promedio = suma / len(vector)
    print(promedio)
    
promediar(resultado, vectorretornado)