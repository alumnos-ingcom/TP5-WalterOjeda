################
# Walter Ojeda - @walter_ojeda
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp5ej1 import ingreso_entero, error_ingreso

def fibonacci(numero):
    num1 = 0
    num2 = 1
    
    for i in range(numero):
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        
    return num2

def prueba():
    ingreso = ingreso_entero("Ingrese un numero: ")
    
    if(ingreso > 2):
        for i in range(ingreso):
            numero = fibonacci(i)
            print(f"{numero}")
    else:
        raise error_ingreso("Numero no valido, intente de nuevo")
    pass

if __name__ == "__main__":
    prueba()