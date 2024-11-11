import random
import Libsort # наш модуль
import time # модуль для замера времени
import sys
sys.setrecursionlimit(10000)
# вставками
def insertion(Massiv):
    Start = time.time()
    Libsort.insertion_sort(Massiv)
    Finish = time.time()
    Res_msec = (Finish-Start)*1000
    return Res_msec
# выбором
def selection(Massiv):
    Start = time.time()
    Libsort.selection_sort(Massiv)
    Finish = time.time()
    Res_msec = (Finish-Start)*1000
    return Res_msec
# сортировка пузырьком
def buble(Massiv):
    Start = time.time()
    Libsort.bubble_sort(Massiv)
    Finish = time.time()
    Res_msec = (Finish-Start)*1000
    return Res_msec
# сортировка быстрая
def quick(Massiv):
    Start = time.time()
    Libsort.quick_sort(Massiv, 0, len(Massiv)-1)
    Finish = time.time()
    Res_msec = (Finish-Start)*1000
    return Res_msec
i = 10
insert =[]
select = []
bubl = []
quik = []
while i !=10**6:
    Massiv = [random.randint(0, 100000) for i in range(i)]
    insert = insert + [round(insertion(Massiv),4)]
    select = select + [round(selection(Massiv),4)]
    bubl = bubl + [round(buble(Massiv),4)]
    quik = quik + [round(quick(Massiv),4)]
    i=i*10

print(f'|Алгоритмы|10|10^2|10^3|10^4|10^5| \n|-|--------|---|\n'
      f'|Вставками|{insert[0]}|{insert[1]}|{insert[2]}|{insert[3]}|'
      f'{insert[4]}|\n|Выбором|{select[0]}|{select[1]}|{select[2]}'
      f'|{select[3]}|{select[4]}|\n|Пузырьком|{bubl[0]}|{bubl[1]}|'
      f'{bubl[2]}|{bubl[3]}|{bubl[4]}|\n|Быстрая|{quik[0]}|{quik[1]}|'
      f'{quik[2]}|{quik[3]}|{quik[4]}|')