################
# Walter Ojeda - @walter_ojeda
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class error_ingreso(Exception):
    pass 

def ingreso_entero(mensaje):

    ingreso = input(mensaje)
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise error_ingreso("la entrada no es valida, reintente ^^") from err
    return entero

def pares_impares(numero):
    
    while numero > 0:
        numero = numero-2
    
    if numero < 0:
        return False
    else:
        return True

def prueba():
    ingrese_numero = ingreso_entero("Ingrese un numero: ")
    
    numero = pares_impares(ingrese_numero)
    
    if numero == True:
        print("Es par")
    else:
        print("Es impar")
pass

if __name__ == "__main__":
    prueba()
