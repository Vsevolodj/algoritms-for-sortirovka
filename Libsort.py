# вставками
def insertion_sort(a):
    for i in range(1, len(a)):
        tmp = a[i]
        j=i-1
        while j >=0 and a[j]>tmp:
            a[j+1]=a[j]
            j-=1
            a[j+1]=tmp
    return a #Возращаем отсортированный массив
# выбором
def selection_sort(a):
    for i in range(len(a) - 1):
        imin = i
        for j in range(i + 1, len(a)):
            if a[j] < a[imin]:
                imin = j
        a[i], a[imin] = a[imin], a[i]
    return a #Возращаем отсортированный массив
# Сортировка пузырьком

def bubble_sort(a):
    n = len(a)
    unordered = True
    while unordered:
        unordered = False
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                unordered = True
    n -= 1
    return a #Возращаем отсортированный массив
#Быстрая сортировка
def quick_sort(arr, low, high):
    if low < high:
        # Разделяем массив и находим индекс опорного элемента
        pivot_index = partition(arr, low, high)

        # Рекурсивно сортируем элементы слева и справа от опорного элемента
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
    return arr #Возращаем отсортированный массив

def partition(arr, low, high):
    pivot = arr[low]  # Опорный элемент — первый элемент подмассива
    i = low + 1  # Начинаем с элемента сразу после pivot

    for j in range(low + 1, high + 1):
        # Если текущий элемент меньше или равен pivot, перемещаем его в "левую часть"
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    # Помещаем pivot на его правильное место в отсортированном массиве
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1  # Возвращаем индекс pivot
