################
# Walter Ojeda - @walter_ojeda
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def distancias(numero1, numero2):
    
    if numero1 >= numero2:
        distancia = numero1 - numero2
    else:
        distancia = numero2 - numero1
        
    return distancia

def prueba():
    numero1 = float(input("ingrese entero: "))
    numero2 = float(input("ingrese entero: "))
    
    total = distancias(numero1, numero2)
    
    print(f"la distancia entre los numeros es {total}")
    
pass

if __name__ == "__main__":
    prueba()