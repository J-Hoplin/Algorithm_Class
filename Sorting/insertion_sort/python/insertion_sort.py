from typing import MutableSequence

def insertion_sort(arr:MutableSequence) -> None:
    for i in range(1,len(arr)):
        loc = i-1
        newItem = arr[i]
        while loc >= 0 and arr[loc] > newItem:
            arr[loc+1] = arr[loc]
            loc-=1
        arr[loc + 1] = newItem

arr = [2,1,4,9,3,8,5,7,6]
insertion_sort(arr)
print(arr)