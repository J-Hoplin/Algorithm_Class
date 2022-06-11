import sys
from typing import Any, Dict,MutableSequence

# https://www.acmicpc.net/problem/2606
def dfs(v:int,g:Dict[int,int]):
    # 방문 여부를 저장한다.
    visited = [False for _ in range(v+1)]
    # 0번째 index값은 어차피 사용 안하므로 총 바이러스에 감염된 컴퓨터를 세는데 사용한다.
    visited[0] = 0
    def aDFS(vertex:int):
        if not visited[vertex]:
            visited[vertex] = True
            visited[0] += 1
            for i in g[vertex]:
                if not visited[i]:
                    aDFS(i)
    # 1번 컴퓨터로부터 시작
    aDFS(1)
    # 1번컴퓨터를 빼고 생각해야하므로 1을 빼준다
    print(visited[0] - 1) 

if __name__ =="__main__":
    # Veretex
    v = int(input())
    # Edge
    e = int(input())
    graph:Dict[int,int] = {x : [] for x in range(1,v+1)}
    for _ in range(e):
        i,j = map(int,sys.stdin.readline().split())
        graph[i].append(j)
        graph[j].append(i)
    dfs(v,graph)