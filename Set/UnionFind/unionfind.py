from typing import Any, MutableSequence

class UnionFind(object):
    def __init__(self):
        pass

    # 부모 노드를 찾는 메소드
    @classmethod
    def getParent(cls,parent:MutableSequence,n:int) -> int:
        if parent[n] == n:
            return n
        return cls.getParent(parent,parent[n])

    # 두 부모 노드를 합치는 함수 : Union연산
    @classmethod
    def unionParent(cls,parent:MutableSequence,n:int,m:int) -> None:
        n = cls.getParent(parent,n)
        m = cls.getParent(parent,m)
        # 부모값을 합칠때는 더 작은 쪽으로 합친다
        if n < m:
            parent[m] = n
        else:
            parent[n] = m

    # 같은 부모를 가지는지 확인한다(같은 그래프에 존재하는지를 구한다)
    @classmethod
    def findParent(cls,parent:MutableSequence,n:int,m:int) -> bool:
        return cls.getParent(parent,n) == cls.getParent(parent,m)

    @classmethod
    def dump(cls,parent) -> None:
        cp = parent[:]
        cp = list(map(lambda x: cls.getParent(parent, x), cp))
        print(*cp)

if __name__ =="__main__":
    parent = [i for i in range(10)]

    union = UnionFind.unionParent
    find = UnionFind.findParent
    dump = UnionFind.dump

    union(parent,1,2)
    union(parent,2,3)
    union(parent,3,4)
    union(parent,5,6)
    union(parent,6,7)
    union(parent,7,8)
    union(parent,8,9)
    print(f"1과 7은 같은 집합인가? : {find(parent,1,7)}")
    union(parent,2,7)
    print(f"1과 7은 같은 집합인가? : {find(parent,1, 7)}")
    dump(parent)

    '''
    1과 7은 같은 집합인가? : False
    1과 7은 같은 집합인가? : True
    0 1 1 1 1 1 1 1 1 1
    
    -> 0번째 인덱스, 즉 0이라는 집합은 없었으므로 0인것이 당연하다. 크루스칼 알고리즘에서 쓰인다.
    '''

