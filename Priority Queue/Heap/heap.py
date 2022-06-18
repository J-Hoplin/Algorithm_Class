'''
Source Code Written by : Hoplin

Written Date : 2022 / 06 / 18
'''
from math import inf
from typing import Any,MutableSequence,Sequence
from collections import deque
from abc import *
from treelib import Node,Tree

class Heap(metaclass=ABCMeta):
    class IlleagalMethodCallException(Exception):
        def __init__(self):
            super().__init__("Illegal Method Call Occured.")

    class ElementNotExistException(Exception):
        def __init__(self):
            super().__init__("Element does not exist in heap")

    class WrongLogicException(Exception):
        def __init__(self):
            super().__init__("Wrong logic exception")

    '''
    < Class Document >
    Heap Class
    
    decide_heapify_algorithm()
    
    Args:
        heap_type (str): Decide heap type(Max heap,Min heap)
    
    Raises:
        WrongConstructorOptionException : Wrong constructor options
    
    build_heap()
    '''

    def __init__(self, heap:MutableSequence) -> None:
        self.infinite = inf
        # Heap Mutable Sequence
        self.heap = deque(heap)
        #최초 실행시 힙으로 만든다
        self.build_heap()

    def build_heap(self) -> None:
        for i in range((len(self.heap) // 2), -1, -1):
            self.heapify(i)

    def return_child_node_indexes(self,k) -> MutableSequence:
        return [(k * 2) + 1, (k * 2) + 2]

    def get_heap_maximum_index(self) -> int:
        return len(self.heap) - 1

    def __str__(self) -> str:
        return f"<{self.__class__.__name__}_Object_{hex(id(self))} {list(self.heap)}>"

    def __call__(self):
        return list(self.heap)

    def getSequence(self) -> MutableSequence:
        return list(self.heap)

    def clearHeap(self) -> None:
        self.heap.clear()

    def search(self,k:int) -> int: # Find index of value 'k'
        k_index = -1
        if k == self.heap[0]:
            return 0
        q = deque(self.return_child_node_indexes(0))
        # BFS operation to tree
        while q:
            index = q.popleft()
            if self.heap[index] == k:
                k_index = index
                break
            else:
                q.extend(list(filter(lambda x: x <= len(self.heap)-1, self.return_child_node_indexes(index))))
        # If not found -> Exception : Element not found
        if k_index == -1:
            raise Heap.ElementNotExistException
        else:
            return k_index

    def convert_heap_type(self) -> object:
        if "Max" in str(self.__class__.__name__):
            from Heap.minHeap import MinHeap
            return MinHeap(self.heap)
        else:
            from Heap.maxHeap import MaxHeap
            return MaxHeap(self.heap)

    def show_in_tree(self):
        t = Tree()
        t.create_node(self.heap[0],0)
        q = deque(self.return_child_node_indexes(0))
        while q:
            index = q.popleft()
            t.create_node(self.heap[index],index,parent=(index-1) // 2)
            q.extend(list(filter(lambda x: x <= len(self.heap) - 1, self.return_child_node_indexes(index))))
        t.show()

    def change_heap_body(self,h:MutableSequence):
        self.clearHeap()
        self.heap.extend(h)
        self.build_heap()

    @abstractmethod
    def trim(self,index:int):
        pass

    @abstractmethod
    def insert(self,k:int):
        pass

    #삭제 연산
    @abstractmethod
    def delete(self,k:int) -> Any:
        pass

    @abstractmethod
    def heapify(self, k:int):
        pass

    @abstractmethod
    def IncreaseKey(self,k:int,v:int):
        pass

    @abstractmethod
    def DecreaseKey(self,k:int,v:int):
        pass

    @abstractmethod
    def ExtractMin(self):
        pass