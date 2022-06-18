'''
Source Code Written by : Hoplin

Written Date : 2022 / 06 / 18
'''

from typing import MutableSequence, Any
from Heap.heap import Heap

class MinHeap(Heap):

    def __init__(self, heap: MutableSequence):
        super().__init__(heap)

    def insert(self,k:int) -> None:
        self.heap.append(k)
        self.trim(len(self.heap) - 1)

    #특정 index를 부모 노드와의 대수비교를 통해 간단 swap연산을 할 때 사용
    def trim(self,index:int) -> None:
        # 루트노드까지만 검사한다.
        while index > 0:
            parent_index = (index - 1) // 2
            # 만약 새로 삽입한 노드의 부모노드 값이 새로 삽입한 노드의 값보다 작은 경우에는 자리를 바꾼다.
            if self.heap[parent_index] > self.heap[index]:
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
                index = parent_index
            else:
                break

    def delete(self,k:int) -> None:
        k_index = self.search(k)
        # change value of k_index to infinite of notes and trim
        # Why infinite of notes? -> Min Heap
        self.heap[k_index] = self.infinite * -1
        self.trim(k_index)
        # Change head and tail value of heap
        self.heap[0],self.heap[len(self.heap)-1] = self.heap[len(self.heap)-1],self.heap[0]
        # Delete element from heap
        self.heap.pop()
        # Root node heapify operation
        self.heapify(0)



    def heapify(self,k:int) -> None:
        # 왼쪽 자식, 오른쪽 자식 노드의 index를 가져온다
        left_child, right_child = self.return_child_node_indexes(k)

        # 이 변수는 두 자식노드들 중 더 작은 값을 가진 노드의 index를 저장하는 변수이다.
        smaller = 0
        # 오른쪽 자식 노드가 범주 내에 있는지 확인한다.
        if right_child <= self.get_heap_maximum_index():
            if self.heap[left_child] < self.heap[right_child]:
                smaller = left_child
            else:
                smaller = right_child
        # 왼쪽 자식 노드만 존재하는 경우이다.
        elif left_child <= self.get_heap_maximum_index():
            smaller = left_child
        # 리프노드 검사에 대해서
        else:
            return
        if self.heap[smaller] < self.heap[k]:
            self.heap[smaller], self.heap[k] = self.heap[k], self.heap[smaller]
            self.heapify(smaller)

    def IncreaseKey(self,k:int,v:int) -> None:
        if k > v:
            raise Heap.WrongLogicException
        k_index = self.search(k)
        self.heap[k_index] = v
        self.heapify(k_index)

    def DecreaseKey(self,k:int,v:int) -> None:
        if k < v:
            raise Heap.WrongLogicException
        k_index = self.search(k)
        self.heap[k_index] = v
        self.trim(k_index)

    def ExtractMin(self) -> int:
        # Min Heap에서는 루트 노드가 가장 작은 값이다.
        # 루트노드값을 저장하고, 0번째 값에 대해 delete연산 수행 후에
        # value를 반환한다.
        value = self.heap[0]
        self.delete(value)
        return value