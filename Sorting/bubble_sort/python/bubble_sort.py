from typing import MutableSequence

def bubble_sort(a:MutableSequence,start,end):
    n = start
    for i in range(start,end-1):
        mi = i
        for j in range(i + 1,end):
            if a[j] < a[mi]:
                mi = j
        a[mi],a[i] = a[i],a[mi]

a = [3,1,2,5,3,4]
bubble_sort(a,0,len(a))
print(a)
