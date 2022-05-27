from time import perf_counter,sleep
import random
import sys

array = random.sample(range(1, 500000), 50000)
print(array, "\n")

#função para ordenar lista aleatória
def quickSort(array, inicio=0, fim= None):
  if fim is None:
    fim = len(array) - 1
  if inicio < fim:
    p = particao(array,inicio,fim)
    quickSortRecursivo(array,inicio,p-1)
    quickSortRecursivo(array,p+1, fim)

def quickSortRecursivo(array, inicio=0, fim= None):
  if fim is None:
    fim = len(array) - 1

def particao(array, inicio, fim):
  pivo = array[fim]
  indexMenores = inicio
  for indexMaiores in range(inicio, fim):
    if array[indexMaiores] <= pivo:
      array[indexMaiores], array[indexMenores] = array[indexMenores], array[indexMaiores]
      indexMenores = indexMenores + 1
  array[indexMenores], array[fim] = array[fim], array[indexMenores]
  return indexMenores
   
              
#ordenando lista aleatória
inicio = perf_counter()
quickSort(array)
fim = perf_counter()
print('\n', array)
print("Tempo duração em segundos :", fim - inicio)


#ordenando lista pior caso
lista=[]
for i in range(0, 50000):
  lista.append(i)
list.reverse(lista)
inicio = perf_counter()
quickSort(lista)
fim = perf_counter()
print("Tempo pior caso duração em segundos :", fim - inicio)