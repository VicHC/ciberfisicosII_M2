#Ejercicio de arreglos desde 1 a n (recibido por la consola)
#y realiza la identificación de los números primos

import sys

global ls

#v = input('Dame el valor n: ')
a = sys.argv[1]

#print(a)
ls = []

def cadena(a):
    for i in range(0,a):
        ls = list.append(i)
        print(ls)
    return cadena
    
cadena(a)
print(ls)
    
#print(str(sys.argv[v]))

# def primos():
#     if n % 2 =! 0 and n % 3 =! 0 
    
#     return primos
    
    