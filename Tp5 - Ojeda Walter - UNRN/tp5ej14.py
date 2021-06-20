################
# Walter Ojeda - @walter_ojeda
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def capicua(numero):
    
    if str(numero) == str(numero)[::-1]:
        return True
    else:
        return False
        

def prueba():
    
    numero = int(input("ingrese un numero entero positivo: "))
    
    if numero > 0:
        resultado = capicua(numero)
        
        if resultado == True:
            print("Es capicua.")
        else:
            print("No es capicua.")
    else:
        print("Numero no valido. Intente de nuevo")
    
if __name__ == "__main__":
    prueba()