from typing import MutableSequence

# min-heap / max-heap은 각자 주석을 변경해보세요

def heap_sort(arr:MutableSequence,n:int):
    build_heap(arr,n)
    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        #heapify_min(arr,0,i-1)
        heapify_max(arr,0,i-1)
    

def build_heap(arr:MutableSequence,n:int):
    for i in range(((len(arr))//2) - 1,-1,-1):
        #heapify_min(arr,i,n)
        heapify_max(arr,i,n)

# min heap
# n : 전체 배열의 크기 의미
def heapify_min(arr:MutableSequence,k:int,n:int):
    left = (k * 2) + 1 #왼쪽 요소
    right = (k * 2) + 2 # 왼쪽 오른쪽 모두 있는 경우
    smaller = None
    # 범주 안에 있는지 확인하는것이다.
    if right <= n:
        if arr[left] < arr[right]:
            smaller = left
        else:
            smaller = right
    elif left <= n: # 왼쪽 노드만 있는경우
        smaller = left
    else: # 오른쪽 왼쪽 모두 없으면 해당 부모 노드가 leaf노드라는 소리이다.
        return
    if arr[smaller] < arr[k]:
        arr[smaller],arr[k] = arr[k],arr[smaller]
        heapify_min(arr,smaller,n)

#max heap
def heapify_max(arr:MutableSequence,k:int,n:int):
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
        arr[k],arr[larger] = arr[larger],arr[k]
        heapify_max(arr,larger,n)

arr = [2,1,4,9,3,8,5,7,6]
heap_sort(arr,len(arr))
print(arr)