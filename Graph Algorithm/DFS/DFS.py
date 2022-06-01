from this import d
from typing import MutableSequence,Any
from collections import deque

# 최대한 책에 있는대로
def DFS_Another(G:dict) -> str:
    visited = dict()
    result = deque([])

    def aDFS(v:Any):
        visited[v] = True
        result.append(v)
        for i in G[v]:
            if not i:
                aDFS(i)
    # 방문 여부에 대한 초기화
    for i in G.keys():
        visited[i] = False
    
    for i,_ in G.items():
        if not visited[i]:
            aDFS(i)

    return ' -> '.join(result)

    
if __name__ == "__main__":
    G = {
        'A': ['B'],
        'B': ['A', 'C', 'H'],
        'C': ['B', 'D'],
        'D': ['C', 'E', 'G'],
        'E': ['D', 'F'],
        'F': ['E'],
        'G': ['D'],
        'H': ['B', 'I', 'J', 'M'],
        'I': ['H'],
        'J': ['H', 'K'],
        'K': ['J', 'L'],
        'L': ['K'],
        'M': ['H']
    }
    print(DFS_Another(G))