from typing import MutableSequence

def selection_sort(arr:MutableSequence) -> None:
    for i in range(len(arr)):
        index = i
        for j in range(i,len(arr)):
            if arr[j] < arr[index]:
                index = j
        arr[i],arr[index] = arr[index],arr[i]
    
arr = [2,1,4,9,3,8,5,7,6]
selection_sort(arr)
print(arr)