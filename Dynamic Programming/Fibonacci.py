from typing import Any, MutableSequence

# 일반적인 피보나치 함수의 재귀횟수
common_fibonacci_recursion_count = 0
# 기억법을 사용한 피보나치 재귀횟수
DP_fibonacci_recursion_count = 0

def Common_Fibonacci(i:int):
    global common_fibonacci_recursion_count
    common_fibonacci_recursion_count += 1
    # 첫번째 혹은 두번째는 모두 값이 1로 시작
    if i == 1 or i == 2:
        return 1
    else:
        return Common_Fibonacci(i - 1) + Common_Fibonacci(i - 2)


def Memorization_Fibonacci(i:int,value_exist:list[int]):
    global DP_fibonacci_recursion_count
    DP_fibonacci_recursion_count += 1
    # 값이 있으면 그 값을 반환한다
    if value_exist[i]:
        return value_exist[i]
    # 첫번째 혹은 두번째는 무조건 1이므로
    if i == 1 or i == 2:
        return 1
    else:
        if not value_exist[i]:
            value_exist[i] = Memorization_Fibonacci(i-1,value_exist) + Memorization_Fibonacci(i-2,value_exist)
        return value_exist[i]

if __name__ == "__main__":
    n = int(input("피보나치수 >> "))
    print("[ 일반적인 피보나치 수열 ]")
    print(f"값 : {Common_Fibonacci(n)}")
    print(f"재귀횟수 : {common_fibonacci_recursion_count}\n")

    print("[ 기억법을 사용한 피보나치 수열 ]")
    print(f"값 : {Memorization_Fibonacci(n,[0 for i in range(n + 1)])}")
    print(f"재귀횟수 : {DP_fibonacci_recursion_count}")

'''
입력값 10

[ 일반적인 피보나치 수열 ]
값 : 55
재귀횟수 : 109

[ 기억법을 사용한 피보나치 수열 ]
값 : 55
재귀횟수 : 17
'''