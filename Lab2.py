import random
import time

def bubblesort(array):
    for i in range(len(array) - 1,0,-1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

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

l=[9,1,1,1,0,0,0,8,10,11,14,2132323,24234524]
x=2

def funkcja(array,a):
    start = time.clock()
    indeks=array
    q=len(array)
    if q==0:
        return "Brak rozwiązań"
    elif q==1:
        return 0
    elif q==2:
        if array[0]>array[1]:
            return 0,1
        else:
            return 1,0
    elif q>=3:
        k=0
        result=[]

        for i in range(q):
            if a < array[i]:
                result.append(array[i])
                k+=1
                if k==3:
                    break
        if k>=1 and k<=3:
            start = time.clock()
            length=len(result)
            bubblesort(result)         #quicksort(result)  
            result.reverse()
            index=[]
            w=0
            while w<length:
                for j in range(length):
                    for z in range(len(indeks)):
                        if result[j]==indeks[z]:
                            index.append(z)
                            w+=1
            end = time.clock()
            total= end-start
            return index,total

        elif k==0:
            return "Brak rezultatów"


print(funkcja(l,x))		#dla tego przypadku quicksort ma krótszy czas sortowania od bubblesort


