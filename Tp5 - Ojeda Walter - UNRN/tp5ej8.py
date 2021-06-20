################
# Walter Ojeda - @walter_ojeda
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def cifrado_cesar(cadena, desplazamiento):
    
    cifrado = ""
    
    for i in cadena:
        
        if i.isupper():
            caracter_numero = ord(i)
            caracter_posicion = ord(i) - ord("A")
            posicion = (caracter_posicion + desplazamiento) % 26
            nueva_posicion = posicion + ord("A")
            nuevo_caracter = chr(nueva_posicion)
            cifrado = cifrado + nuevo_caracter
            
        elif i.islower():
            caracter_numero = ord(i)
            caracter_posicion = ord(i) - ord("a")
            posicion = (caracter_posicion + desplazamiento) % 26
            nueva_posicion = posicion + ord("a")
            nuevo_caracter = chr(nueva_posicion)
            cifrado = cifrado + nuevo_caracter
        elif i.isdigit():
            numero_nuevo = (int(i) + desplazamiento) % 10
            cifrado = cifrado + str(numero_nuevo)
        else:
            cifrado = cifrado + i
               
    return cifrado

def desencriptado_cesar(cadena, desplazamiento):
    desencriptado = ""
    for i in cadena:
        if i.isupper():
            caracter_numero = ord(i)
            caracter_posicion = ord(i) - ord("A")
            posicion = (caracter_posicion - desplazamiento) % 26
            nueva_posicion = posicion + ord("A")
            nuevo_caracter = chr(nueva_posicion)
            desencriptado = desencriptado + nuevo_caracter
            
        elif i.islower():
            caracter_numero = ord(i)
            caracter_posicion = ord(i) - ord("a")
            posicion = (caracter_posicion - desplazamiento) % 26
            nueva_posicion = posicion + ord("a")
            nuevo_caracter = chr(nueva_posicion)
            desencriptado = desencriptado + nuevo_caracter
        elif i.isdigit():
            nuevo_numero = (int(i) - desplazamiento) % 10
            desencriptado = desencriptado + str(nuevo_numero)
        else:
            desencriptado = desencriptado + i
            
    return desencriptado
    
    
def prueba():
    eleccion = input('Bienvenido ^^, Precione "C" para encriptar o "D" para desencriptar: ')
    
    if eleccion == "c" or eleccion =="C":
        texto = input("Ingrese texto para encriptar: ")
        desplazamiento = int(input("Ingrese desplazamiento: "))
        resultado = cifrado_cesar(texto, desplazamiento)
        print(resultado)
    
    elif eleccion == "d" or eleccion == "D":
        texto = input("Ingrese texto para desencriptar: ")
        desplazamiento = int(input("Ingrese el desplazamiento: "))
        resultado = desencriptado_cesar(texto, desplazamiento)
        print(resultado)
        
    else:
        print("La opcion no es valida, intente de nuevo ^^")
        
pass
    
if __name__ == "__main__":
    prueba()