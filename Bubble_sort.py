from time import perf_counter,sleep
import random



array = random.sample(range(1, 50000), 1000)
print(array)

#função para ordenar lista aleatória
def bubbleSort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


#função para colocar em pior caso
def bubbleSortPiorCaso(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


              
#ordenando lista aleatória
inicio = perf_counter()
bubbleSort(array)
fim = perf_counter()
print('\n', array)

print("Tempo duração em segundos :", fim - inicio)


#ordenando lista pior caso
bubbleSortPiorCaso(array)
inicio = perf_counter()
bubbleSort(array)
fim = perf_counter()
print('\n', array)

print("Tempo duração em segundos :", fim - inicio)