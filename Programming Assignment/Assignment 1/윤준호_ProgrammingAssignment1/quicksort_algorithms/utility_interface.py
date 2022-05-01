from abc import *

'''
Source Code Written By Hoplin(윤준호)
Github : https://github.com/J-hoplin1

Last Edited Date : 2022 / 04 / 29
'''

# Common utility abstract class
class utility(metaclass=ABCMeta):
    def __init__(self):
        # Set access modifier as 'private'
        self.__comparison = 0

    def getComparisonCount(self) -> int:
        return self.__comparison

    def clearComparisonCount(self) -> None:
        self.__comparison = 0

    def addComparison(self) -> None:
        self.__comparison += 1

    @abstractmethod
    def sort(self,arr,startIndex,endIndex):
        #Override this method
        pass