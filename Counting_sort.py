from time import perf_counter,sleep
import random

array = random.sample(range(1, 500000), 10000)


#função para ordenar lista aleatória
def countingSort(array):
  maiorEntrada=max(array)
  indices = [0] * (maiorEntrada + 1)
  cont = [0] * (maiorEntrada + 1)
  for i in range (len(indices)):
    indices[i] = i
    cont[i] = 0
    
  for i in range (len(array)):
    cont[indices[array[i]]] = cont[indices[array[i]]] + 1
  for i in range (1,len(cont),1):
    cont[i] = cont[i-1]+cont[i]


  saida = [0] * len(array)

  for i in range ((len(array))):
    saida[cont[indices[array[i]]]-1] = array[i]
    cont[indices[array[i]]] = cont[indices[array[i]]] -1 

  print(saida)


    
#ordenando lista aleatória
inicio = perf_counter()
countingSort(array)
fim = perf_counter()
print("Tempo duração em segundos :", fim - inicio)


#ordenando lista pior caso
lista=[]
for i in range(10000, 0,-1):
  lista.append(i)
inicio = perf_counter()
countingSort(lista)
fim = perf_counter()
print("Tempo duração em segundos :", fim - inicio)