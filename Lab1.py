import random
#Lista1
L1=[]
L2=[]
for i in range(20):
    x1=random.randint(0,20)
    x2=random.randint(0,20)
    L1.append(x1)
    L2.append(x2)
print(L1)
print(L2)

def bubblesort(array):
    for i in range(len(array) - 1,0,-1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

bubblesort(L1)
print(L1)

def quicksort(array, l=0, r=None):
    if r is None:
        r = len(array) - 1
    i, j = l, r
    pivot = random.choice(array)
    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    if l < j:
        quicksort(array, l, j)
    if r > i:
        quicksort(array, i, r)

quicksort(L2)
print(L2)