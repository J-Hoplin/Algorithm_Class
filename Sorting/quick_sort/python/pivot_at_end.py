from typing import MutableSequence

def pivot_at_end(arr:MutableSequence,startIndex,endIndex):
    '''
    만약 기준값이 끝값인 경우
    '''
    p = arr[endIndex]
    i = startIndex - 1
    for j in range(startIndex,endIndex):
        if arr[j] <= p:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i + 1],arr[endIndex] = arr[endIndex],arr[i + 1]
    return i + 1

def quick_sort(arr:MutableSequence,startIndex,endIndex):
    if startIndex < endIndex:
        standard = pivot_at_end(arr,startIndex,endIndex)
        quick_sort(arr,startIndex,standard-1)
        quick_sort(arr,standard+1,endIndex)
    else:
        pass

arr = [2,1,4,9,3,8,5,7,6]
quick_sort(arr,0,len(arr)-1)
print(arr)