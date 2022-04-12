from typing import MutableSequence

def pivot_at_start(arr:MutableSequence,startIndex,endIndex):
    '''
    만약 기준값이 시작값인 기준
    '''
    p = arr[startIndex]
    i = startIndex
    for j in range(startIndex + 1, endIndex):
        if arr[j] <= p:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i],arr[startIndex] = arr[startIndex],arr[i]
    return i

def quick_sort(arr:MutableSequence,startIndex,endIndex):
    if startIndex < endIndex:
        standard = pivot_at_start(arr,startIndex,endIndex)
        quick_sort(arr,startIndex,standard-1)
        quick_sort(arr,standard + 1, endIndex)
    else:
        pass

arr = [2,1,4,9,3,8,5,7,6]
quick_sort(arr,0,len(arr))
print(arr)