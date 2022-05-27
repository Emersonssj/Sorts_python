from time import perf_counter,sleep
import random
from functools import reduce

array = random.sample(range(1, 1000000), 100000)


#função para ordenar lista aleatória
def radixSort(array, qtdDigitos):
  for i in range(0, qtdDigitos):   #varredura por algorismo
    balde = [[]for j in range(10)]
    for item in array:
      algorismo = item // 10 ** (i) % 10
      balde[algorismo].append(item)
    array = combinar(balde)
  


#função para calcular a quantidade de digitos
def calcularDigitos(array):
  m = 0
  for i in array:
    m = max(m,i)
  return len(str(m))


#função para combinar os baldes
def combinar(array):
  return reduce(lambda x, y: x + y, array)


#ordenando lista aleatória
qtdDigitos = calcularDigitos(array)
inicio = perf_counter()
radixSort(array,qtdDigitos)
fim = perf_counter()
print("Tempo duração em segundos :", fim - inicio)


#ordenando lista pior caso
#array=[]
#for i in range(100000, 0,-1):
#  array.append(i)
#qtdDigitos = calcularDigitos(array)
#inicio = perf_counter()
#radixSort(array, qtdDigitos)
#fim = perf_counter()
#print("Tempo duração em segundos :", fim - inicio)