import random

def Ordenamiento_Burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista



if __name__ == '__main__':
    Tamano_de_lista = int(input('De que tamaño sera la lista? '))

    lista = [random.randint(0,100) for i in range(Tamano_de_lista)]
    print(lista)

    lista_ordenada = Ordenamiento_Burbuja(lista)
    print(lista_ordenada)
