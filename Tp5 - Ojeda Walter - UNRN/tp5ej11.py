################
# Walter Ojeda - @walter_ojeda
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def promedio_movil(lista, cantidad):
    numeros = 0
    contador = 0
    
    for i in lista:
        if contador < cantidad:
            numeros= numeros + i
            contador += 1
        
    promedio = numeros/cantidad
    
    return promedio

def prueba():
    lista = [5, 10, 15, 20, 10, 20]
    cantidad = int(input("Ingrese cantidad a promediar: "))
    
    promediot = promedio_movil(lista, cantidad)
    
    print(f"El promedio movil es {promediot}")
    
if __name__ == "__main__":
    prueba()