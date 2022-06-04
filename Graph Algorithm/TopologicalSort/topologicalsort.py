from typing import Any, MutableSequence, Dict
from collections import deque

def topologicalSort(size:int,G:Dict[int,MutableSequence]) -> None:
    # 각정점의 차수를 담고있는 배열
    nodeInDegree = [0 for _ in range(size + 1)]
    # 넘겨받은 그래프에서 각 노드들이 연결된 노드들에 대해 진입차수를 더해준다.
    for _, j in G.items():
        for l in j:
            nodeInDegree[l] += 1

    # 차수가 0인 노드들이 들어가는 큐이다
    zeroDegreeNodeQueue = deque([])
    #결과를 저장하는 큐
    result = deque([])

    # 초기에 진입차수가 0인 노드들을 큐에 넣는다.
    for i in range(1,size + 1):
        if nodeInDegree[i] == 0:
            zeroDegreeNodeQueue.append(i)

    # 모든 노드들을 방문하기 때문에 노드 개수만큼의 순회만 필요하다
    for _ in range(size):
        # 진행 과정에서 차수가 0인 노드가 아예 없는경우는 사이클이 발생했다는 의미이다.
        # 위상정렬은 사이클이 없는 유향그래프가 기본 전제 조건이다.
        if not zeroDegreeNodeQueue:
            print("사이클이 발생했습니다. 위상정렬이 불가능합니다.")
            return
        # 차수가 0인 노드들중 하나를 뺀다
        n = zeroDegreeNodeQueue.popleft()
        result.append(n)

        # 진입 차수 0인 노드들에 대해서 진출간선을 끊어준다
        for j in G[n]:
            # 진입차수가 0인 노드가 진입간선이었던 노드들에 대해 차수를 1씩 뺴준다.
            nodeInDegree[j] -= 1
            # 만약 제거 후 노드의 차수가 0이 된다면 큐에 넣는다
            if not nodeInDegree[j]:
                zeroDegreeNodeQueue.append(j)

    print(*result)

if __name__ == "__main__":
    graph = {
        1 : [2,5],
        2 : [3],
        3 : [4],
        4 : [6],
        5 : [6],
        6 : [7],
        7 : []
    }
    topologicalSort(max(list(graph.keys())),graph)