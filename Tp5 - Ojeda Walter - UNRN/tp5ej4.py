################
# Walter Ojeda - @walter_ojeda
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp5ej1 import ingreso_entero, error_ingreso

def numeros_perfectos(numero):
    suma = 0 
    
    for i in range(1, numero):
        if numero % i == 0:
            suma = suma + i
    
    if suma == numero:
        return True
    else:
        return False

def prueba():
    ingreso = ingreso_entero("ingrese un numero: ")
    
    if ingreso > 0:
        numero = numeros_perfectos(ingreso)
        
        if numero is True:
            print("Es un numero perfecto")
            
        else:
            print("No es un numero perfecto")
        
    else:
        raise error_ingreso("El numero no es valido, intente de nuevo")
    
    pass
    
if __name__ == "__main__":
    prueba()