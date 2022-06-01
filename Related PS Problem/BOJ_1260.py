# https://www.acmicpc.net/problem/1260
from collections import deque
import sys
from typing import MutableSequence,Any

'''
그래프를 DFS,BFS로 각각 탐색한 결과를 출력하는 프로그램 작성

방문할 수 있는 정점이 여러개 -> 정점 번호가 작은것을 우선적으로 방문한다
더이상 방문할 수 있는 점이 없는경우 종료

첫째줄에 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V가 주어진다.M개의 줄에는 간선이 연결하는 
두 정점의 번호가 주어진다.


<생각할 예외>

시작 정점에서 연결된 정점이 없는경우

'''

def DFS(graph:dict,starting_node:Any):
    def aDFS(node:Any):
        visited_stack.append(node)
        for i in graph[node]:
            if i not in visited_stack:
                aDFS(i)
    visited_stack = list()
    aDFS(starting_node)
    print(" ".join(map(str,visited_stack)))    

def BFS(graph:dict,starting_node:Any):
    visited_queue = deque([])
    result = list()
    result.append(starting_node)
    visited_queue.extend(graph[starting_node])
    while visited_queue:
        n = visited_queue.popleft()
        if n not in result:
            result.append(n)
            visited_queue.extend(graph[n])
    print(" ".join(map(str,result)))
    
if __name__ == "__main__":
    graph = dict()
    vertex,edge,starting_node = list(map(int,sys.stdin.readline().split()))
    for i in range(1,vertex + 1):
        graph[i] = list()
    for _ in range(edge):
        i,j = list(map(int,sys.stdin.readline().split()))
        graph[i].append(j)
        graph[j].append(i)
    for i,j in graph.items():
        graph[i] = sorted(j)
    DFS(graph,starting_node)
    BFS(graph,starting_node)