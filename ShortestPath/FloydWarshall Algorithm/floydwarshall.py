import math,traceback
from typing import Any, MutableSequence
# 무한대는 math.inf로 정의한 후 이를 inf로 사용
inf = math.inf


# Dynamic Progarmming의 원리를 이용한다
def floydWarshall(size:int,Graph:MutableSequence) -> None:

    # 경로를 출력하는 Clojure선언
    def printFloydWarshallPath():
        for i in range(size):
            print(*floydWarshallPath[i])

    # size * size 크기의 이차원 배열
    # 초기화를 위한 임의의 이차원배열
    floydWarshallPath = [[0 for _ in range(size)] for _ in range(size)]


    # 받은 그래프 경로들의 정보를 가지고 초기화를 진행한다
    for i in range(size):
        for j in range(size):
            floydWarshallPath[i][j] = Graph[i][j]

    # k : 거쳐가는 모든 노드들을 의미한다
    for k in range(size):
        for i in range(size):
            for j in range(size):
                if floydWarshallPath[i][j] > (floydWarshallPath[i][k] + floydWarshallPath[k][j]):
                    floydWarshallPath[i][j] = floydWarshallPath[i][k] + floydWarshallPath[k][j]
        print(f"Node {k + 1}를 지나가는 경우")
        printFloydWarshallPath()
        print()

    print("결과")
    printFloydWarshallPath()
    

if __name__ == "__main__":
    Graph = [
        [0,5,inf,8],
        [7,0,9,inf],
        [2,inf,0,4],
        [inf,inf,3,0]
    ]
    floydWarshall(len(Graph),Graph)