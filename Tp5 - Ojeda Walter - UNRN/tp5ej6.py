################
# Walter Ojeda - @walter_ojeda
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def parentesis_balanceados(cadena):
    contador = 0
    
    for i in cadena:
        if i == "(":
            contador = contador + 1
        elif i == ")":
            contador = contador - 1
            
    if contador == 0:
        return True
    else:
        return False
    
    
def prueba():
    cadena = input("Ingrese texto: ")
    
    resultado = parentesis_balanceados(cadena)
    
    if resultado == True:
        print("OK")
        
    else:
        print("NOT OK")

if __name__ == "__main__":
    prueba()