from typing import MutableSequence

def bubble_sort(a:MutableSequence,start,end):
    n = start
    for i in range(start,end-1):
        exchange = False # 내부 순환에서 교환이 이루어졌는지 확인
        for j in range(i + 1,end):
            if a[j-1] > a[j]:
                a[j-1],a[j]= a[j],a[j-1]
                exchange = True
        #일어나지 않았다는것은 정렬이 완료됐다는 의미이므로 종료
        if not exchange:
            break

a = [3,1,2,5,3,4]
bubble_sort(a,0,len(a))
print(a)
