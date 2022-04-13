from typing import MutableSequence

def bubble_sort(a:MutableSequence,start,end):
    n = start
    for i in range(start,end-1):
        for j in range(i + 1,end):
            if a[j-1] > a[j]:
                a[j-1],a[j]= a[j],a[j-1]

a = [3,1,2,5,3,4]
bubble_sort(a,0,len(a))
print(a)
