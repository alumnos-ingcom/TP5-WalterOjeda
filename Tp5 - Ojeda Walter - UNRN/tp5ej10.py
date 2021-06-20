################
# Walter Ojeda - @walter_ojeda
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def binario(numero):
    if numero <= 0:
        return "0"
    
    binario = ""
    
    while numero > 0:
        residuo = int(numero % 2)
        numero = int(numero / 2)
        binario = str(residuo) + binario
    return binario

def decifrar_binario(numero):
    
    posicion = 0
    decimal = 0
    numero = numero[::-1]
    for i in numero:
        multiplicador = 2 ** posicion
        decimal += int(i) * multiplicador
        posicion += 1
        
    return decimal

def prueba():
    opcion = input('Ingrese "B" si desea convertir a binario o ingrese "D" para convertir a decimal: ')
    
    if opcion is 'B' or opcion is 'b':
        
        decimal = int(input("Ingresa un número decimal: "))
        binario_resultado = binario(decimal)
        print(f"El número {decimal} es {binario_resultado} en binario")
        
    elif opcion is 'D' or opcion is 'd':
        
        decimal = input("ingrese su numero binario: ")
        decimal_resultado = decifrar_binario(decimal)
        print(f"El numero {decimal} es {decimal_resultado}")
    
    else:
        print("Opcion no valida, intente de nuevo.")

if __name__ == "__main__":
    prueba()