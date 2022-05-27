from time import perf_counter,sleep
import random

array = random.sample(range(1, 200000), 100000)
print(array)


def bucketSort(array):
    valorMaximo = max(array)
    tamanho = valorMaximo/len(array)

    listaDeBaldes= []
    for x in range(len(array)):
        listaDeBaldes.append([]) 

    for i in range(len(array)):
        j = int (array[i] / tamanho)
        if j != len (array):
            listaDeBaldes[j].append(array[i])
        else:
            listaDeBaldes[len(array) - 1].append(array[i])

    for z in range(len(array)):
        insertion_sort(listaDeBaldes[z])
            
    saida = []
    for x in range(len (array)):
        saida = saida + listaDeBaldes[x]
    print(saida)

def insertion_sort(balde):
    for i in range (1, len (balde)):
        var = balde[i]
        j = i - 1
        while (j >= 0 and var < balde[j]):
            balde[j + 1] = balde[j]
            j = j - 1
        balde[j + 1] = var



#ordenando lista aleatória
#inicio = perf_counter()
#bucketSort(array)
#fim = perf_counter()
#print("Tempo duração em segundos :", fim - inicio)


#ordenando lista pior caso
lista=[]
for i in range(100000, 0,-1):
  lista.append(i)
inicio = perf_counter()
bucketSort(lista)
fim = perf_counter()
print("Tempo duração em segundos :", fim - inicio)