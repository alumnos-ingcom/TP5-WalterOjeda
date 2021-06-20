################
# Walter Ojeda - @walter_ojeda
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def busqueda_palabras(cadena, palabra):
    
    indice = cadena.find(palabra)
    
    return indice
    
def prueba():
    
    cadena = input("ingrese una frase o cadena: ")
    palabra = input("ingrese busqueda: ")
    
    posicion = busqueda_palabras(cadena, palabra)
    
    print(f"la palabra {palabra}, se encuentra en la posicion {posicion}.")
    
if __name__ == "__main__":
    prueba()