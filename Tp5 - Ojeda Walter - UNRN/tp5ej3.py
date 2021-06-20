################
# Walter Ojeda - @walter_ojeda
# UNRN Andina - Introducción a la Ingenieria en Computación
################

######################
# 3. ¡Tribonacci!
# La secuencia de Tribonacci es el mismo concepto que la de Fibonacci común,
# pero acá en lugar de sumar dos terminos; se suman de a tres.
# Los tres primeros terminos son uno y el termino 4 es la suma de los tres anteriores.
# Implementar una funcion que permita obtener el n-esimo termino de la suceción Tribonacci,
# siendo este termino un numero entero positivo mayor a 3.
######################

from tp5ej1 import ingreso_entero, error_ingreso

def tribonacci(numero):
    num1 = 0
    num2 = 0
    num3 = 1
    
    for i in range(numero):
        num4 = num1 + num2 + num3
        num1 = num2
        num2 = num3
        num3 = num4
        
    return num3

    
def prueba():
    ingreso = ingreso_entero("Ingrese un numero: ")
    
    if ingreso > 3:
        for i in range(ingreso):
            numero = tribonacci(i)
            print(f"{numero}")
    else:
        raise error_ingreso("Numero no valido, intente de nuevo")
    pass

if __name__ == "__main__":
    prueba()