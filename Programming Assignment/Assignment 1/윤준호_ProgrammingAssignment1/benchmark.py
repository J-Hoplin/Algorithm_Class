import os,platform,time,math,random,pprint,json,copy
from typing import Any,MutableSequence
from quicksort_algorithms.recursive_quicksort import recursive_qsorts
from quicksort_algorithms.Interactive_quicksort import interactive_qsorts
from quicksort_algorithms.randomized_quicksort import randomized_qsorts
from quicksort_algorithms.utility_interface import utility

'''
Source Code Written By Hoplin(윤준호)
Github : https://github.com/J-hoplin1

Last Edited Date : 2022 / 04 / 29
'''

class algorithm_tester(object):
    test_set = list(map(int, [math.pow(10, 2), math.pow(10, 4), math.pow(10, 6)]))
    def __init__(self):
        self.resultJSON = dict()
        self.testCase = None
        # 최초 인스턴스 실행시
        self.generateTestSet()

    def dumpToJSON(self):
        with open("result.json",'w') as f:
            json.dump(self.resultJSON,f,indent=4)

    # Generate Test case
    def generateTestSet(self) -> None:
        res = dict()
        for p, i in enumerate(algorithm_tester.test_set):
            sets = list()
            for j in range(1, 21):
                arr = random.sample([p for p in range(1, i + 1)], j)
                random.shuffle(arr)
                sets.append(arr)
            res[f"Test_case_{p + 1}"] = sets
        self.testCase = res


    def test_data(self,sortingInstance : utility,caseName:str,substractOneEndIndex:bool=False) -> None:
        result = dict()
        '''
        Document about test_data(function : function)
        
        :parameter
        
        sortingInstance
        - Type : Class - utility
        - Get instance of sorting algorithm class's instance. This will be operate via polymorphism trait as parent type 'utility'
        
        substractOneEndIndex
        - Type : bool
        - Default Value : False
        - Decide wether end index need to be substract 1. If True, endIndex will be substract 1 in first execution
        '''

        # 테스트 데이터를 복사하여 정렬을 한다.
        copy_test = copy.deepcopy(self.testCase)

        for p, i in copy_test.items():
            # Initiate essential variables
            arr = []
            previous = []
            resultCapsule = dict()
            for j,l in enumerate(i):
                arr = l
                previous = arr[:]  # Deep Copy random testset. This may occur overhead while testing

                # Time estimate start
                start = time.perf_counter()

                if substractOneEndIndex:
                    sortingInstance.sort(arr,0, len(arr)-1)  # Get comparison count as result value
                else:
                    sortingInstance.sort(arr, 0, len(arr))

                # Time estimate end
                end = time.perf_counter() - start

                # 측정 시간이 매우 작아 지수표현이 들어간다. 1000을 곱해 지수표현 없앤다.
                resultCapsule[f"GroupSet_{j+1}"] = {
                    "SortingTime": end,
                    "previous": previous,
                    "sorted": arr,
                    "comparisonCount": sortingInstance.getComparisonCount()
                }
                # 각 테스트 케이스마다 comparison count를 비워준다.
                sortingInstance.clearComparisonCount()
            result[f"{p}"] = resultCapsule

        self.resultJSON[caseName] = result

    def stream(self):
        # 재귀 퀵정렬
        recursive_sort = recursive_qsorts()
        # 순환 퀵정렬
        interactive_sort = interactive_qsorts()
        # 랜덤 퀵정렬
        randomized_sort = randomized_qsorts()
        print("""
            Algorithm Programming Assignment #1

            < Quick Sort Cases > 
            1. Recursive Quicksort
            2. Interactive Quicksort 
            3. Randomized Quciksort

            < Test Cases - Representative >
            1. 10 ** 2
            2. 10 ** 4
            3. 10 ** 6


            """)
        print("Benchmarking Case1 : Recursive Quick Sort - Pivot at End\n")
        self.test_data(recursive_sort, "Recursive")
        print("\nBenchmarking Case2 : Iterative Quick Sort\n")
        self.test_data(interactive_sort, "Iterative")
        print("\nBenchmarking Case3 : Randomized Quick Sort\n")
        self.test_data(randomized_sort, "Randomized", True)
        print("Convert Result to Json\n")
        self.dumpToJSON()

        print("[ Used test data set will be shown at below ] \n")

        for i,j in self.testCase.items():
            print(f"< {i} >")
            for q,t in enumerate(j):
                print(f"Randomly Pick {q + 1} elements : {t}")
            print()




if __name__ == "__main__":
    platf = platform.system()
    at = algorithm_tester()
    if platf == "Windows":
        os.system('cls')
    else:
        os.system('clear')
    at.stream()