# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

modo_por_defecto = "lento"
lista = [1,2,3,4,5,6,7,8,9,10]
personas = ["Sara", "Pedro", "Miguel"]

def resta(a,b,algoritmo="estandar",modo=None):
    """ Devuelve el resultado de la operación b-a
        modo -> velocidad de ejecución: lento, rapido, aproximado
        algoritmo -> algoritmo a utilizar """
    #pass #si queremos dejar una función vacía
    if modo is None:
        modo = modo_por_defecto #MEJOR opción que evaluar con un modo por defecto, así se puede cambiar ese modo por consola, y a que no se pasa como atributo
    print("{} - {} según el algoritmo {} en modo {} = {}".format(b,a,algoritmo,modo,b-a))
    return b-a
    
def es_par(x):
    return x%2==0

def es_impar(x):
    return not es_par(x)

def mi_filter(condicion,lista):
    b = []
    for numero in lista:
        if condicion(numero):
            b.append(numero)
    return b
    
def cuadrado(x):
    return x**2

    
""" MAIN """
print(resta(5, 4, "alg1"))
print(resta(5, 4, "alg1", "rapido"))
print(resta(5, 4, modo="rapido"))

#filter
print(list(filter(es_par,lista)))
print(list(map(cuadrado,lista)))

#funcion lambda: para cosas sencillas sin necesidad de crear una funcion aparte
print(list(filter(lambda x:x%2==0,lista)))
print(list(map(lambda x:x**2,lista)))

#listas por compresion
print([x ** 2 for x in lista])
print([x ** 2 for x in lista if x % 2 == 0])

#tupla por compresion
print(tuple(p[0] for p in personas))

#diccionarios por compresion
print({p: len(p) for p in personas})