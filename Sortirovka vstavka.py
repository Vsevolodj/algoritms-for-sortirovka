def insertion_sort(a):
    for i in range(1, len(a)):
        tmp = a[i]
        j=i-1
        while j >=0 and a[j]>tmp:
            a[j+1]=a[j]
            j-=1
            a[j+1]=tmp
# проверим
a = [int(x) for x in input().split()]
insertion_sort(a)
print(a)
