from typing import MutableSequence,Any

def build_heap(arr: MutableSequence, n: int):
    for i in range(((len(arr)) // 2) - 1, -1, -1):
        # heapify_min(arr,i,n)
        heapify_max(arr, i, n-1)

# max heap
def heapify_max(arr: MutableSequence, k: int, n: int):
    left = (k * 2) + 1
    right = (k * 2) + 2
    larger = None
    if right <= n:
        if arr[left] > arr[right]:
            larger = left
        else:
            larger = right
    elif left <= n:
        larger = left
    else:
        return

    if arr[larger] > arr[k]:
        arr[k], arr[larger] = arr[larger], arr[k]
        heapify_max(arr, larger, n)

# 요소 삽입
def enque(arr:MutableSequence,value):
    arr.append(value)
    build_heap(arr,len(arr))

#요소 빼기
def deque(arr:MutableSequence) -> Any:
    arr[0],arr[len(arr)-1] = arr[len(arr)-1],arr[0]
    res = arr.pop()
    build_heap(arr,len(arr))

arr = [2, 1, 4, 9, 3, 8, 5, 7, 6]
build_heap(arr,len(arr))
enque(arr,3) #[9, 7, 8, 6, 3, 4, 5, 1, 2, 3]
deque(arr) #[8, 7, 5, 6, 3, 4, 3, 1, 2]
