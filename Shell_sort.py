from time import perf_counter,sleep
import random

array = random.sample(range(1, 500000), 100000)


#função para ordenar lista aleatória
def shellSort(array):
    n = len(array)
    intervalo = n // 2
    while intervalo > 0:
        for i in range(intervalo, n):
            temp = array[i]
            j = i
            while j >= intervalo and array[j - intervalo] > temp:
                array[j] = array[j - intervalo]
                j -= intervalo

            array[j] = temp
        intervalo //= 2
    return array


    
#ordenando lista aleatória
inicio = perf_counter()
shellSort(array)
fim = perf_counter()
print("Tempo duração em segundos :", fim - inicio)


#ordenando lista pior caso
lista=[]
for i in range(100000, 0,-1):
  lista.append(i)
inicio = perf_counter()
shellSort(lista)
fim = perf_counter()
print("Tempo duração pior caso em segundos :", fim - inicio)