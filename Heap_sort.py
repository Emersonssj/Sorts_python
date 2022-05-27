from time import perf_counter,sleep
import random
from functools import reduce

array = random.sample(range(1, 1000000), 100000)


#função para ordenar um heap - raiz e 2 folhas
def heapify(array, n, i):
    longo = i  
    esq = 2 * i + 1   
    dir = 2 * i + 2    

    if esq < n and array[longo] < array[esq]:
        longo = esq

    if dir < n and array[longo] < array[dir]:
        longo = dir

    if longo != i:
        array[i], array[longo] = array[longo], array[i]
        heapify(array, n, longo)
 
def heapSort(array):
    n = len(array)

    for i in range(n//2 - 1, -1, -1):
        heapify(array, n, i)

    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
  
  
#n = tamanho 
#ordenando lista aleatória
tamanho = len(array)
inicio = perf_counter()
heapSort(array)
fim = perf_counter()
print("Tempo duração em segundos :", fim - inicio)



#ordenando lista pior caso
array=[]
for i in range(100000, 0,-1):
  array.append(i)
inicio = perf_counter()
heapSort(array, )
fim = perf_counter()
print("Tempo duração pior caso em segundos :", fim - inicio)