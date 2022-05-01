from typing import MutableSequence
from collections import deque
from .utility_interface import utility

'''
Source Code Written By Hoplin(윤준호)
Github : https://github.com/J-hoplin1

Last Edited Date : 2022 / 04 / 29
'''


class interactive_qsorts(utility):
    '''
    Document

    For Interactive QuickSort(순차적 퀵정렬)

    call __doc__ magic method to view class document
    '''

    def __init__(self):
        super().__init__()

    #Override Method
    def sort(self,arr:MutableSequence,startIndex:int,endIndex:int) -> None:
        # 피벗 기준으로 나누어진 startIndex,endIndex가 저장될 스택이다.
        stack = deque([endIndex,startIndex])
        # 스택이 비어있을때까지 순회를 한다
        while stack:
            # start Index
            p = stack.pop()
            # end Index
            r = stack.pop()
            # p == r 이라는 것은 이미 정렬이 완료된 특정 원소를 가리킨다는 의미가 되므로
            if p < r:
                pivot = arr[p]
                i = p
                for j in range(p + 1, r):
                    # +1 Comparison count
                    self.addComparison()
                    if arr[j] < pivot:
                        i += 1
                        arr[i],arr[j] = arr[j],arr[i]

                arr[i],arr[p] = arr[p], arr[i]


                #Left Partition
                if i != p:
                    stack.append(i) #왼쪽 부분의 끝 index
                    stack.append(p) # 왼쪽 부분의 시작 index
                #Right Partition
                if r != i + 1:
                    stack.append(r) # 오른쪽 부분의 끝 index
                    stack.append(i+1) # 오른쪽 부분의 시작 index
            else:
                pass

'''
a =[31,8,48,73,11,3,20,29,65]
Interactive_quick_sort(a,0,len(a))
print(a)

'''

