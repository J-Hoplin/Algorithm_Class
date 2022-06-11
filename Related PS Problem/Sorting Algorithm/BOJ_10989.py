import sys
from typing import *

#계수정렬
#최소한의 배열로 작성하기

n = int(input())
res = [0] * 10001 
for i in range(n):
    inp = int(sys.stdin.readline())
    res[inp] += 1
for j in range(10001):
    if res[j] != 0:
        for _ in range(res[j]):
            print(j)