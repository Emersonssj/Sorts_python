from time import perf_counter,sleep
import random


array = random.sample(range(1, 50000), 1000)
print(array)

#função para ordenar lista aleatória
def selectionSort(array):
  length = len(array)
  for j in range(length-1):
    pivo = j
    for i in range(j,length):
      if array[i]<array[pivo]:
        pivo = i
    if array[j]>array[pivo]:
      aux = array[j]
      array[j] = array[pivo]
      array[pivo] = aux


#função para colocar em pior caso
def selectionSortPiorCaso(array):
  length = len(array)
  for j in range(length-1):
    pivo = j
    for i in range(j,length):
      if array[i]>array[pivo]:
        pivo = i
    if array[j]<array[pivo]:
      aux = array[j]
      array[j] = array[pivo]
      array[pivo] = aux


              
#ordenando lista aleatória
inicio = perf_counter()
selectionSort(array)
fim = perf_counter()
print('\n', array)

print("Tempo duração em segundos :", fim - inicio)


#ordenando lista pior caso
selectionSortPiorCaso(array)
inicio = perf_counter()
selectionSort(array)
fim = perf_counter()
print('\n', array)

print("Tempo duração em segundos :", fim - inicio)