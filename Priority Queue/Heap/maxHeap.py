'''
Source Code Written by : Hoplin

Written Date : 2022 / 06 / 18
'''
from typing import MutableSequence, Any
from collections import deque
from Heap.heap import Heap

class MaxHeap(Heap):

    def __init__(self, heap: MutableSequence):
        super().__init__(heap)

    def insert(self,k:int) -> None:
        self.heap.append(k)
        self.trim(len(self.heap) - 1)

    #특정 index를 부모 노드와의 대수비교를 통해 간단 swap연산을 할 때 사용한다.
    def trim(self,index:int) -> None:
        # 루트노드까지만 검사한다.
        while index > 0:
            parent_index = (index - 1) // 2
            # 만약 새로 삽입한 노드의 부모노드 값이 새로 삽입한 노드의 값보다 작은 경우에는 자리를 바꾼다.
            if self.heap[parent_index] < self.heap[index]:
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
                index = parent_index
            else:
                break

    def delete(self,k:int) -> None:
        # get k's index
        k_index = self.search(k)
        # change value of k_index to inf(infinite) and trim
        self.heap[k_index] = self.infinite
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
        # 이 변수는 두 자식노드들 중 더 큰 값을 가진 노드의 index를 저장하는 변수이다.
        larger = 0
        # 오른쪽 자식 노드가 범주 내에 있는지 확인한다
        if right_child <= self.get_heap_maximum_index():
            if self.heap[left_child] < self.heap[right_child]:
                larger = right_child
            else:
                larger = left_child
        # 왼쪽 자식 노드만 존재하는 경우에 해당한다
        elif left_child <= self.get_heap_maximum_index():
            larger = left_child
        # 왼쪽 오른쪽 자식 노드들이 범주에 속하지 않는 값들인 경우 함수 종료. 즉 리프노드를 검사할때를 의미한다.
        else:
            return
        # 자식 노드들 중 더 큰것들과 부모 노드의 크기를 비교한다. max heap이므로 만약 자식노드가 크면 자식노드를 올리고 아닌 경우에는 유지한다
        if self.heap[larger] > self.heap[k]:
            # 이 분기문을 들어왔다는 것은 부모노드와 자식노드의 자리를 바꿨음을 의미한다. 그렇기 때문에, 바꾼 노드에 대해서 heapify를 진행하여 힙 조건을 만족한다
            self.heap[larger], self.heap[k] = self.heap[k], self.heap[larger]
            self.heapify(larger)

    # 키값 k를 가진 원소의 키값을 증가된 키 값 v로 바꾼다
    def IncreaseKey(self,k:int,v:int) -> None:
        # 최대힙에서 키값이 증가된 경우에는 부모노드와 대수비교로 swap만 해주면 된다.
        # If k is larger than v
        if k > v:
            raise Heap.WrongLogicException
        k_index = self.search(k)
        self.heap[k_index] = v
        self.trim(k_index)

    # 키값 k를 가진 원소의 키 값을 감소된 키 값 v로 바꾼다.
    def DecreaseKey(self,k:int,v:int) -> None:
        # 최대힙에서 키값이 감소된 경우에 대해서는 heapify를 진행해준다.
        # If v is larger than k
        if k < v:
            raise Heap.WrongLogicException
        k_index = self.search(k)
        self.heap[k_index] = v
        self.heapify(k_index)

    # 가장 키 값이 작은 원소 키 값을 제거하고 그 키값을 리턴한다.
    def ExtractMin(self) -> int:
        value = self.heap[0]
        q = deque(self.return_child_node_indexes(0))
        # Tree BFS
        while q:
            index = q.popleft()
            if self.heap[index] < value:
                value = self.heap[index]
            q.extend(list(filter(lambda x: x <= len(self.heap) - 1, self.return_child_node_indexes(index))))
        self.delete(value)
        return value
