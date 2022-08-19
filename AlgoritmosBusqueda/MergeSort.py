import random

def MergeSort(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print(izquierda, '+' * 5, derecha)
        #llamada recursiva en cada mitad
        MergeSort(izquierda)
        MergeSort(derecha)

        #Iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        #Iterador para lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            
            k += 1
        
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
        print(f'Izquierda {izquierda}, Derecha {derecha}')
        print(lista)
        print('-' * 50)
    return lista

if __name__ == '__main__':
    Tamano_de_lista = int(input('De que tamaño sera la lista? '))

    lista = [random.randint(0,100) for i in range(Tamano_de_lista)]
    print(lista)
    print('-' * 20)

    lista_ordenada = MergeSort(lista)
    print(lista_ordenada)