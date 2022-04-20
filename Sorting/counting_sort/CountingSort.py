from typing import *

#계수정렬
#관련 문제 : https://www.acmicpc.net/problem/10989

def CountingSort(arr: MutableSequence) -> MutableSequence:
    # 반환배열(배열 B) : 입력배열과 동일한 길이의 배열이어야 한다
    returnArray = [0] * (len(arr)+1)
    # 각 요소가 몇개있는지에 대해 (배열 C) : 최대값만큼의 길이여야 한다.
    countingArray = [0] * (max(arr) + 1)
    for i in range(max(arr)+1):
        countingArray[i] = 0

    print("Loop 1 - Array B : ",countingArray)
    # 각 값이 index가 되는곳에 + 1씩 해준다 (배열 C)
    for i in arr:
        countingArray[i] += 1

    print("Loop 2 - Array C : ",countingArray)
    # 각 값의 개수 누적 배열로 변환 (배열 C')
    for i in range(1, len(countingArray)):
        countingArray[i] += countingArray[i - 1]

    print("Loop 3 - Array C' : ", countingArray)
    #값의 누적에 따른 값들의 자리 찾기
    for j in arr[::-1]: 
        returnArray[countingArray[j]] = j
        countingArray[j] -= 1

    print("Loop 4 - Array B : ",returnArray)
    return returnArray[1:]

if __name__ == "__main__":
    '''
    Loop 1 - Array B :  [0, 0, 0, 0, 0, 0, 0, 0]
    Loop 2 - Array C :  [0, 2, 2, 2, 1, 2, 0, 1]
    Loop 3 - Array C' :  [0, 2, 4, 6, 7, 9, 9, 10]
    Loop 4 - Array B :  [0, 1, 1, 2, 2, 3, 3, 4, 5, 5, 7]
    [1, 1, 2, 2, 3, 3, 4, 5, 5, 7]
    '''
    a = [5,2,3,1,4,2,3,5,1,7]
    print(CountingSort(a))
