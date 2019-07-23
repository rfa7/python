"""
Recursive function.
There is a list of numbers. We adding those numbers to next box, and this two sets must be identical.
We got a first occurence in our list and we using function to append to new list rest from original location (list).
"""
lista = [1,2,3,4,5,6,7,8]
start = 1
podano = [1]
def podaj(start, lista):
    if len(lista) <= 1+start*2:
        print("KONIEC")
        # tu podano procedura
        lista = lista[start:]
        podano.append(lista[:])
        print(podano)
        return podano
    new = start*2
    lista = lista[start:]
    podano.append(lista[0:new])
    print('nowy start :', new, ' podano: ', podano)
    podaj(new,lista)

podaj(start,lista)
