from typing import MutableSequence,Any
from collections import deque
import math
inf = math.inf

def Prim(startingpoint:int,G:MutableSequence) -> None:
    # 결과 큐에 끝난 순서대로 넣는다.
    def addToResultQueue(node:int) -> None:
        result.append(f"Node {node + 1}")

    # 가장 짧은 거리의 간선을 선택한다.
    def getShortestCostNode() -> int:
        min = inf
        index = 0
        for i in range(size):
            if (not visited[i]) and (costs[i] < min):
                min = costs[i]
                index = i
        return index

    # Vertex의 총 개수이다.
    size = len(G)
    # 결과가 순서대로 저장되는 Queue이다.
    result = deque([])
    #각 정점의 비용을 무한대로 초기화 한다
    costs = [inf for _ in range(size)]
    #방문이 된 노드인지에 대한 판별
    visited = [False for _ in range(size)]


    # 시작점의 cost를 0으로 초기화 한다.
    costs[startingpoint] = 0
    # 시작점을 방문한 상태로 변경한다
    visited[startingpoint] = True
    addToResultQueue(startingpoint)
    # 시작 지점의 정점들에 대해서 cost를 초기화 한다.
    for i in range(len(G[startingpoint])):
        costs[i] = G[startingpoint][i]

    # size - 1 : 최초 노드에 대해서는 실행을 했기 때문에, 순회 횟수에서 1을 빼준다
    # 그래도 총 V개수만큼 순회하는것과 동일하다
    for _ in range(size - 1):
        # 가장 Cost가 적은 노드를 선택한다.
        nextNode = getShortestCostNode()
        # 해당 노드를 방문처리를 한다
        visited[nextNode] = True
        # 해당 노드를 방문 순서를 맞추기 위해  결과에 저장한다
        addToResultQueue(nextNode)
        # 해당 노드에 연결된 노드들에 대해서 검사를 한다
        for j in range(size):
            # 방문하지 않은 노드들에 대해서
            if not visited[j]:
                # 만약 기존의 cost보다 이 노드로부터 연결할 수 있는 cost가 더 적다면
                # 이 노드를 통해 연결하는 cost로 변경한다.
                if costs[j] > G[nextNode][j]:
                    costs[j] = G[nextNode][j]
    print(' -> '.join(result))


if __name__ =="__main__":
    graph = [
        [0, 2, 5, 1, inf, inf],
        [2, 0, 3, 2, inf, inf],
        [5, 3, 0, 3, 1, 5],
        [1, 2, 3, 0, 1, inf],
        [inf, inf, 1, 1, 0, 2],
        [inf, inf, 5, inf, 2, 0]
    ]
    Prim(0, graph)