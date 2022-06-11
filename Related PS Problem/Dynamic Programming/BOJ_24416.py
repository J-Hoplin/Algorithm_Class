import sys
from typing import Any

# 시간때문에 pypy3로 제출할것
sys.setrecursionlimit(10**6)

count1 = 1 # 최초 호출에 대한 Count
count2 = 0

def fib(n:int) -> None:
    global count1
    if(n == 1 or n == 2):
        return 1
    count1 += 1
    return (fib(n-1) + fib(n-2))

def fibonacci(n:int) -> None:
    global count2
    x = [0 for _ in range(n+1)]
    x[0] = x[1] = 1
    for i in range(3,n+1):
        count2 += 1
        x[i] = x[i-1] + x[i-2]
    return x[n]

if __name__ =="__main__":
    n = int(input())
    fib(n)
    fibonacci(n)
    print(f"{count1} {count2}")