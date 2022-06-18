'''
Source Code Written by : Hoplin

Written Date : 2022 / 06 / 18
'''
from Heap.heap import Heap
from typing import MutableSequence
from Heap.maxHeap import MaxHeap
from Heap.minHeap import MinHeap

class PriorityQueue(object):
    """
    < Class Document : Priority Queue >

    - 부모클래스 : object
    - 의존성 : Heap,MaxHeap,MinHeap

    < Exception Class >

    - WrongConstructorOptionException
        Description:
            PriortyQueue생성자에게 heap_type매개변수를 넘길때 잘못된 타입을 넘기게 될 경우에 이 예외가 발생됩니다

    < Methods >

    - __init__(self,initial_sequence:MutableSequence,heap_type:str="max")
        Description:
            생성자 클래스입니다
        Args:
            initial_sequence: 초기화하고싶은 우선순위 큐를 넘겨줍니다. MutableSequence타입이어야 합니다
            heap_type: heap 종류를 선택합니다. 매개변수는 "max", "min" 만 분기할 수 있습니다
        Raises:
            PriorityQueue.WrongConstructorOptionException

    - __str__(self)
        Description:
            객체 정보 문자열을 반환합니다

    - __call__(self)
        Description:
            큐를 리스트로 반환합니다

    - insert(self,k)
        Description:
            큐에 k를 추가합니다
        Args:
            k: 큐에 추가할 값입니다

    - delete(self,k)
        Description:
            큐에서 k를 제거합니다
        Args:
            k: 큐에서 제거할 값입니다.

    - extractMin(self)
        Description:
            큐에서 키값이 가장 작은 원소의 키 값을 제거하고, 그 키값을 리턴합니다

    - increase_key(self,k:int,v:int)
        Description:
            키값 k를 가진 원소의 키 값을 증가된 키 값 v로 바꿉니다.
        Args:
            k: 기존 키값
            v: 증가된 키값
        Rasies:
            Heap.WrongLogicException

    - decrease_key(self,k:int,v:int)
        Description:
            키값 k를 가진 원소의 키 값을 증가된 키값 v로 바꿉니다.
        Args:
            k: 기존 키값
            v: 증가된 키값
        Raises:
            Heap.WrongLogicException

    - convert_heap_type(self)
        Description:
            Heap Type을 변경합니다.

    -
    """
    # Exception class about __init__ 'heaptype' parameter
    class WrongConstructorOptionException(Exception):
        def __init__(self):
            super().__init__("Wrong type of constrctor error.")

    def __init__(self,initial_sequence:MutableSequence,heap_type:str="max"):
        heap_type = heap_type.lower()
        self.heap = ""
        # Apply Priority Queue Polymorphic Type
        if heap_type == "max":
            self.heap = MaxHeap(initial_sequence)
        elif heap_type == "min":
            self.heap = MinHeap(initial_sequence)
        else:
            raise PriorityQueue.WrongConstructorOptionException

    def __str__(self) -> str:
        return f"<{self.__class__.__name__}_Object_{hex(id(self))} {self.heap()}>"

    def __call__(self) -> MutableSequence:
        return self.heap()

    def insert(self,k) -> None:
        self.heap.insert(k)

    def delete(self,k) -> None:
        self.heap.delete(k)

    def extractMin(self) -> int:
        return self.heap.ExtractMin()

    def increase_key(self,k:int,v:int) -> None:
        self.heap.IncreaseKey(k,v)

    def decrease_key(self,k:int,v:int):
        self.heap.DecreaseKey(k,v)

    def clear_queue(self):
        self.heap.clearHeap()

    def convert_heap_type(self):
        self.heap = self.heap.convert_heap_type()

    def show_in_tree(self):
        self.heap.show_in_tree()

    def change_queue_body(self,q:MutableSequence):
        self.heap.change_heap_body(q)