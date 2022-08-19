from ast import Return
import random

def busqueda_Binaria(lista, comienzo, final, objetivo, contador):
    
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    if comienzo > final:
        print(f'Resuelto en {contador} Pasos')
        return False

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        print(f'Resuelto en {contador} Pasos')
        return True
    elif lista[medio] < objetivo:
        contador +=1
        return busqueda_Binaria(lista, medio + 1, final, objetivo, contador)
    else:
        contador +=1
        return busqueda_Binaria(lista, comienzo, medio - 1, objetivo, contador)



if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar en la lista? '))
    contador = 1
    lista = sorted([random.randint(0, 100) for i in range (tamano_de_lista)])

    encontrado = busqueda_Binaria(lista, 0, len(lista), objetivo, contador)
    print(lista)
    print(f'El elemento {objetivo} {"Esta" if encontrado else "no esta"} en la lista')