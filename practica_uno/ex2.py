#Ejercicio de arreglos desde 1 a n (recibido por la consola)
#y realiza la identificación de los números primos

import sys

global ls
ls = [] 

a = int(sys.argv[1]) # Se aloja el valor recibido en consola en posición específica en tipo entero.

# Función para crear lista de números desde 1 a n
def cadena(a):
    
    # En caso de que el valor introducido sea menor a 1 (cero o valor negativo),
    # no será admitido por el código.
    if a < 1:
        print('Ingresa valores positivos únicamente.')
    
    # Función específica (ciclo) para añadir números en un rango de 1 a n, a una lista.
    for i in range(1, a+1):
        
        ls.append(i) # Agrega el valor de i a la lista hasta llegar a rango máximo.
        
    return ls

print('Lista de numeros de 1 hasta n: ')
print(cadena(a)) # Imprime la función donde se alojan los números hasta el rango especificado


# Función para reconocimiento de números primos.
def primos(a):
    
    c_div = 0 # Contador para identificar si un número ya ha sido dividido.
    
    # Ciclo para revisión de cada número en la lista
    for n in range(1, a): 
        
        # Ciclo de división para reconocer numeros primos 
        if a % n == 0:
            c_div += 1
            if c_div > 1:
                return False
    return True

        

lprim = [] # Lista para alojar números primos

# Ciclo para añadir número primo a lista
for v in ls: 
    if primos(v):
        lprim.append(v)

print('Los números primos de la lista son: ')
print(lprim) # Imprime lista de números primos
