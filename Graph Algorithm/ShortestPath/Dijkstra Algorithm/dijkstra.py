import sys
import math
from typing import Any, MutableSequence

# 무한대
inf = math.inf


def Dijkstra(size: int, start: int, G: MutableSequence):
    # 최소 거리를 가진 노드를 선택하는 Clojure
    def getShortestDistanceNode() -> int:
        min = inf
        index = 0
        for i in range(size):
            if (not visited[i]) and (distance[i] < min):
                min = distance[i]
                index = i
        return index

    # 해당 노드가 방문이 된 노드인지에 대해
    visited: list[bool] = [False for _ in range(size)]
    # 각 노드들의 최단거리
    distance: list[int] = [0 for _ in range(size)]

    # 시작지점을 기준으로 초기 최단 거리를 초기화해준다
    for i in range(len(G[start])):
        distance[i] = G[start][i]

    # 시작지점을 방문상태로 변경해 준다
    visited[start] = True

    # -2 : 처음 시작하는 시작점과 마지막 노드에 대해서는 수행해 줄 필요가 없기 때문이다.
    for i in range(size - 2):
        print("-" * 15)
        print(f"검사 이전 최단경로 테이블 : {distance}")
        # 최단 방문하지 않은 군집중 최단거리 노드를 가져온다
        nextVisit = getShortestDistanceNode()
        # 해당 노드를 방문처리한다
        visited[nextVisit] = True

        # 전체 노드에 대해서 검사를 한다
        for j in range(size):
            # 방문하지 않은 노드들에 대해서
            # 방문을 한 상태에서는 출발지점 기준, 최단거리가 이미 구해졌다는 의미이기 때문이다
            if not visited[j]:
                # 기존의 거리보다 최근 방문한 노드까지의 경로 + 노드에서 검사중인 노드까지의 거리가 더 짧으면 갱신한다.
                if (distance[nextVisit] + graph[nextVisit][j]) < distance[j]:
                    distance[j] = distance[nextVisit] + graph[nextVisit][j]

        print(f"선택된 노드 : {nextVisit + 1}")
        print(f"검사 이후 최단경로 테이블 : {distance}")
        print("-" * 15)
    print(*distance)

if __name__ == "__main__":
    size = 6
    # 0 : 자기자신을 의미
    graph = [
        [0, 2, 5, 1, inf, inf],
        [2, 0, 3, 2, inf, inf],
        [5, 3, 0, 3, 1, 5],
        [1, 2, 3, 0, 1, inf],
        [inf, inf, 1, 1, 0, 2],
        [inf, inf, 5, inf, 2, 0]
    ]
    Dijkstra(size, 0, graph)

'''
---------------
검사 이전 최단경로 테이블 : [0, 2, 5, 1, inf, inf]
선택된 노드 : 4
검사 이후 최단경로 테이블 : [0, 2, 4, 1, 2, inf]
---------------
---------------
검사 이전 최단경로 테이블 : [0, 2, 4, 1, 2, inf]
선택된 노드 : 2
검사 이후 최단경로 테이블 : [0, 2, 4, 1, 2, inf]
---------------
---------------
검사 이전 최단경로 테이블 : [0, 2, 4, 1, 2, inf]
선택된 노드 : 5
검사 이후 최단경로 테이블 : [0, 2, 3, 1, 2, 4]
---------------
---------------
검사 이전 최단경로 테이블 : [0, 2, 3, 1, 2, 4]
선택된 노드 : 3
검사 이후 최단경로 테이블 : [0, 2, 3, 1, 2, 4]
---------------
0 2 3 1 2 4
'''