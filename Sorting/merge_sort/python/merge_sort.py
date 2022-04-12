from turtle import right
from typing import MutableSequence

def merge_sort(arr:MutableSequence,lindex : int,rindex : int):
    if lindex < rindex:
        middle = (lindex + rindex) // 2
        merge_sort(arr,lindex,middle)
        merge_sort(arr,middle+1,rindex)
        merge(arr,lindex,middle,rindex)

def merge(arr:MutableSequence,lindex:int,middle:int,rindex:int):
    l = lindex # 왼쪽 시작 인덱스
    r = middle + 1 # 오른쪽 시작 인덱스
    t = 0 # temp index
    temp = [None] * ((rindex - lindex) + 1)
    while l <= middle and r <= rindex:
        if arr[l] < arr[r]:
            temp[t] = arr[l]
            t += 1
            l += 1
        else:
            temp[t] = arr[r]
            t += 1
            r += 1
    while l <= middle:
        temp[t] = arr[l]
        l += 1
        t += 1
    while r <= rindex:
        temp[t] = arr[r]
        r += 1
        t += 1
    t = 0
    while(lindex <= rindex):
        arr[lindex] = temp[t]
        t += 1
        lindex += 1
        
arr = [2,1,4,9,3,8,5,7,6]
merge_sort(arr,0,len(arr) - 1)
print(arr)