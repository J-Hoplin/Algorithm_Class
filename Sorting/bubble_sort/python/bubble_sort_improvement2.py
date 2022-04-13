from typing import MutableSequence

def bubble_sort(a:MutableSequence,start,end):
    n = start
    lastChangedIndex = 0 # 가장 마지막으로 교환이 일어난 index

    while lastChangedIndex < end -1:
        last = end-1 # 만약 교환이 아예 없었다면, last에 계속 end-1이 유지될 것이다.
        for i in range(lastChangedIndex + 1,end):
            if a[i - 1] > a[i]:
                a[i],a[i-1] = a[i-1],a[i]
                last = i
        lastChangedIndex = last

a = [3,1,2,5,3,4]
bubble_sort(a,0,len(a))
print(a)
