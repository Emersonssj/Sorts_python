from time import perf_counter,sleep
import random

array = random.sample(range(1, 50000), 15000)
print(array)

#função para ordenar lista aleatória
def insertionSort(array):
  tamanhoArray = len(array)
  for i in range(1,tamanhoArray):
    aux = array[i]
    j = i - 1
    while j >= 0 and array[j] > aux:
      array[j+1] = array[j]
      j=j-1
    array[j+1] = aux


def insertionSortPiorCaso(array):
  tamanhoArray = len(array)
  for i in range(1,tamanhoArray):
    aux = array[i]
    j = i-1
    while j >= 0 and array[j] < aux:
      array[j+1] = array[j]
      j = j-1
    array[j+1] = aux

              
#ordenando lista aleatória
inicio = perf_counter()
insertionSort(array)
fim = perf_counter()
print('\n', array)

print("Tempo duração em segundos :", fim - inicio)


#ordenando lista pior caso
insertionSortPiorCaso(array)
inicio = perf_counter()
insertionSort(array)
fim = perf_counter()
print('\n', array)

print("Tempo duração em segundos :", fim - inicio)