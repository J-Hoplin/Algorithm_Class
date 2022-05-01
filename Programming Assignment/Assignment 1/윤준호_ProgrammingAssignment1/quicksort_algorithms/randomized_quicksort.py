from typing import MutableSequence
from random import randint
from .utility_interface import utility


'''
Source Code Written By Hoplin(윤준호)
Github : https://github.com/J-hoplin1

Last Edited Date : 2022 / 04 / 29
'''

class randomized_qsorts(utility):

    '''
    Document

    For Randomized QuickSort(랜덤 피벗 퀵정렬)

    call __doc__ magic method to view class document
    '''

    def __init__(self):
       super().__init__()

    # Override Method
    def sort(self,arr:MutableSequence,startIndex:int,endIndex:int) -> None:
        pl,pr = self.randomPivot(arr,startIndex,endIndex)
        if startIndex < pr:
            self.sort(arr,startIndex,pr)
        if endIndex > pl:
            self.sort(arr,pl,endIndex)

    def randomPivot(self,arr:MutableSequence,startIndex:int,endIndex:int) -> MutableSequence:
        randIndex = randint(startIndex,endIndex)
        pivot = arr[randIndex]
        pl = startIndex
        pr = endIndex
        while pl <= pr:
            while arr[pl] < pivot:
                pl += 1
            while arr[pr] > pivot:
                pr -= 1
            if pl <= pr:
                arr[pl],arr[pr] = arr[pr],arr[pl]
                pl += 1
                pr -= 1
            # + 1 Comparison count
            self.addComparison()
        return [pl,pr]

'''
t = randomized_qsorts()
a = [31,8,48,73,11,3,20,29,65]
print(a)
t.randomized_pivot_qsort(a,0,len(a)-1)
print(a)
'''