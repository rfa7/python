"""
Recursive function.
There is a list of numbers. We adding those numbers to next box, and this two sets must be identical.
We got a first occurence in our list and we using function to append to new list rest from original location (list).
"""

w = int(input('Put your number, please: '))
lista = [x for x in range(1,w+1)]
print('List starts with:', lista[0], 'List ends:', lista[-1])
start = 1
podano = [1]
n = 0


def podaj(start, lista, n):
    if len(lista) <= 1+start*2:
        print("_________The END__________")
        lista = lista[start:]
        if len(lista) > 0:
            for i in lista:
                podano.append(i)
            n += 1
        print(podano)
        print('Last added element:', podano[-1])
        print('Start No:', start,'|| N:', n, '|| N^^2 IS:',2**n, '|| Between...',
              2**n, 'and ...', 2**(n+1))
        return podano
    lista = lista[start:]
    new = start*2
    for i in lista[0:new]:
        podano.append(i)
    podaj(new,lista, n+1)

podaj(start,lista, n)
