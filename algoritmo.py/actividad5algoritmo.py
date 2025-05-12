def bubble_sort(lista):
    length = len(lista)
    for i in range(length):
        for j in range(0, (length-i) - 1):

            if lista[j] > lista[j + 1]:
                auxiliar = lista[j + 1]
                lista[j + 1] = lista[j]
                lista[j] = auxiliar
    return lista


lista_desordenada = [3, 6, 7, 8, 3, 45, 23, 0, 16, 26, 6, 7, 50]
lista_ordenada = bubble_sort(lista_desordenada)
print(lista_ordenada) # output: [0, 3, 3, 6, 6, 7, 7, 8, 16, 23, 26, 45, 50]