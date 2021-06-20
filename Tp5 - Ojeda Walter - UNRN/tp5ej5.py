################
# Walter Ojeda - @walter_ojeda
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp5ej1 import ingreso_entero, error_ingreso

def inversion_mayusculas(cadena):
    cambio = cadena.swapcase()
    return cambio

def prueba():
    cadena_ingreso = input("Ingrese una frase: ")
    cambio = inversion_mayusculas(cadena_ingreso)
    print(cambio)
    pass

if __name__ == "__main__":
    prueba()