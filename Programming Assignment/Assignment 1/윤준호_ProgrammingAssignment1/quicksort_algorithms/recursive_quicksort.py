from typing import MutableSequence
from .utility_interface import utility


'''
Source Code Written By Hoplin(윤준호)
Github : https://github.com/J-hoplin1

Last Edited Date : 2022 / 04 / 29
'''

class recursive_qsorts(utility):
    '''
    Document

    For Recursive QuickSort(재귀적 퀵정렬)

    call __doc__ magic method to view class document
    '''

    def __init__(self):
        super().__init__()

    # Pivot at end
    # Override Method
    def sort(self, arr: MutableSequence, startIndex: int, endIndex: int) -> None:
        if startIndex < endIndex:
            standard = self.pivot_at_end(arr, startIndex, endIndex)
            self.sort(arr, startIndex, standard)
            self.sort(arr, standard + 1, endIndex)

    def pivot_at_end(self, arr: MutableSequence, startIndex: int, endIndex: int) -> int:
        '''
        기준이 맨 뒤 요소인 경우
        '''
        pivot = arr[endIndex - 1]
        i = startIndex - 1
        for j in range(startIndex, endIndex - 1):

            # +1 Comparison Count
            self.addComparison()

            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[endIndex - 1] = arr[endIndex - 1], arr[i + 1]
        return i + 1


    # Pivot at start
    def quick_sort_pivot_start(self,arr:MutableSequence, startIndex:int, endIndex:int) -> None:
        if startIndex < endIndex:
            standard = self.pivot_at_start(arr,startIndex,endIndex)
            self.quick_sort_pivot_start(arr,startIndex,standard)
            self.quick_sort_pivot_start(arr,standard + 1, endIndex)

    def pivot_at_start(self,arr:MutableSequence, startIndex:int, endIndex:int) -> int:
        '''
        기준이 맨 처음 요소인 경우
        '''
        pivot = arr[startIndex]
        i = startIndex
        for j in range(startIndex + 1, endIndex):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j],arr[i]

                # +1 Comparison Count
                self.addComparison()

        arr[i],arr[startIndex] = arr[startIndex], arr[i]
        return i







'''
a = [31,8,48,73,11,3,20,29,65]
quick_sort_pivot_end(a,0,len(a))
#quick_sort_pivot_start(a,0,len(a))
print(a)
'''