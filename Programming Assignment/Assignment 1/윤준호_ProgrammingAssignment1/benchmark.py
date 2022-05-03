import os,platform,time,math,random,pprint,json,copy,threading
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
    #Class methods
    start = 0
    end = 0
    test_set = list(map(int, [math.pow(10, 2), math.pow(10, 4),math.pow(10,6)]))

    def __init__(self):
        self.resultJSON = dict()
        self.testCase = None


    @classmethod
    def start_record(cls) -> None:
        algorithm_tester.start = time.time()
    @classmethod
    def end_record(cls) -> None:
        algorithm_tester.end = time.time()


    def dumpToJSON(self,serializer,json_name) -> None:
        with open(f"{json_name}.json",'w') as f:
            json.dump(serializer,f,indent=4)

    # Generate Test case
    def generateTestSet(self) -> None:
        res = dict()
        for p, i in enumerate(algorithm_tester.test_set):
            sets = list()
            for _ in range(1, 21):
                arr = [random.randint(1,i) for _ in range(i)]
                sets.append(arr)
            res[f"Test_case_{p + 1}"] = sets
        self.testCase = res

    # Define access modifier as private
    def __test_data(self,sortingInstance : utility,caseName:str,substractOneEndIndex:bool=False) -> None:
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

                resultCapsule[f"GroupSet_{j+1}"] = {
                    "SortingTime": end,
                    "comparisonCount": sortingInstance.getComparisonCount()
                }
                # 각 테스트 케이스마다 comparison count를 비워준다.
                sortingInstance.clearComparisonCount()
            result[f"{p}"] = resultCapsule
        self.resultJSON[caseName] = result

    def stream(self) -> None:
        # 최초 인스턴스 실행시
        print("Generating Test Data Sets...\n")
        self.generateTestSet()

        qsort_instances = {
            "Recursive": [recursive_qsorts(), False],# 재귀 퀵정렬
            "Iterative": [interactive_qsorts(), False],# 순환 퀵정렬
            "Randomized": [randomized_qsorts(), True],# 랜덤 퀵정렬
        }

        for i,j in qsort_instances.items():
            instance, third_parameter = j
            self.__test_data(instance, i, third_parameter)
            print(f"Benchmarking : {i} Quick Sort... \n")

        '''
        recursive_sort = recursive_qsorts()
        iterative_sort = interactive_qsorts()
        randomized_sort = randomized_qsorts()
        print("Benchmarking Case1 : Recursive Quick Sort - Pivot at End...\n")
        self.__test_data(recursive_sort,"Recursive")
        print("\nBenchmarking Case2 : Iterative Quick Sort...\n")
        self.__test_data(iterative_sort,"Iterative")
        print("\nBenchmarking Case3 : Randomized Quick Sort...\n")
        self.__test_data(randomized_sort,"Randomized",True)
        '''

        '''
        threads = []

        for i,j in qsort_instances.items():
            instance,third_parameter = j
            newThread = threading.Thread(target=self.__test_data,args=(instance,i,third_parameter))
            newThread.start()
            pid = newThread.native_id
            print(f"Start Thread[pid : {pid}] : Benchmarking {i} Quick Sort... ")
            threads.append(newThread)

        for i in threads:
            i.join()
        '''


        print("\nConvert Test Case to JSON...")
        self.dumpToJSON(self.testCase, "Used_test_case")
        print("\nConvert Result to JSON...\n")
        self.dumpToJSON(self.resultJSON,"result")
        algorithm_tester.end_record()
        print(f"Benchmark Complete! Total execution time {(algorithm_tester.end - algorithm_tester.start):0.2f}sec")



if __name__ == "__main__":
    platf = platform.system()
    at = algorithm_tester()
    if platf == "Windows":
        os.system('cls')
    else:
        os.system('clear')
    at.start_record()
    at.stream()