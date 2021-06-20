################
# Walter Ojeda - @walter_ojeda
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def comparar_lista(lista1, lista2):
    
    if set(lista1) == set(lista2):
        return True
    else:
        return False


def prueba():
    lista1 = [1, 2, 3, 4, 5]
    lista2 = [5, 4, 2, 3, 1]
    
    resultado = comparar_lista(lista1, lista2)
    
    if resultado == True:
        print("Verdadero.")
    else:
        print("Falso.")

if __name__ == "__main__":
    prueba()