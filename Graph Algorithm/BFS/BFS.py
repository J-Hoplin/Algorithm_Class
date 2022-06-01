from typing import Any, MutableSequence
from collections import deque


# 최대한 책 내용대로
def BFS_Another(G: dict, s: Any) -> str:
    visited = dict()
    for i in G.keys():
        visited[i] = False
    check_queue = deque([])
    result_queue = deque([])
    check_queue.append(s)
    while check_queue:
        n = check_queue.popleft()
        if not visited[n]:
            visited[n] = True
            result_queue.append(n)
            check_queue.extend(G[n])
    return ' -> '.join(result_queue)

# 일반적 구현
def BFS(G: dict, s: Any) -> str:
    # 방문 여부를 판단하는 Queue
    visited = deque([])
    # 방문이 끝난 순서대로 판단을 한다.
    check_queue = deque([])
    # 첫 시작노드를 방문 검사 큐에 넣어줍니다
    check_queue.append(s)

    # 검사 큐가 비어있을때 까지
    while check_queue:
        n = check_queue.popleft()
        if n not in visited:
            visited.append(n)
            # Python Tip
            # List(Type : MutableSequence)의 extend를 사용하여 MutableSequence객체를 append하면
            # Unpacking하여 들어갑니다
            check_queue.extend(G[n])

    return ' -> '.join(visited)


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
    # A -> B -> C -> H -> D -> I -> J -> M -> E -> G -> K -> F -> L
    print(BFS(G, 'A'))
    print(BFS_Another(G,'A'))