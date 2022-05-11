import traceback
from typing import Any

# Node Class
class Node(object):
    def __init__(self,key) -> None:
        self.key = key # Key value of Node
        self.left = None # Left tree of Node
        self.right = None # Right tree of Node

# Binary Search Class
class BST(object):

    class AlreadyExistException(Exception):
        def __init__(self, msg:str) -> None:
            pass
    
    class NotExistException(Exception):
        def __init__(self, msg:str) -> None:
            pass

    def __init__(self, root:Node) -> None:
        self.root = root
        self.root_key = self.root.key
    
    # BST 검색
    def search(self,root : Node,x : Any):
        # root의 key값이 Null 이거나(검색실패)
        # root의 key값이 x와 일치할때(검색성공)
        if (not root) or (root.key == x):
            return True

        # 찾고자 하는 키값이 root보다 큰 경우
        if root.key < x:
            return self.search(root.right,x)
        # 찾고자 하는 키값이 root보다 작은 경우
        else:
            return self.search(root.left,x)
    

    def insert(self,x) -> bool:
        return self.insert_working(x,self.root)

    def insert_working(self,x,root:Node) -> None:
        # 이진검색 트리에서 삽입을 하기 위해서 이진 검색트리에 x를 키값으로 가진 노드가 없어야 한다.
        if root.key == x:
            raise BST.AlreadyExistException(f"value '{root.key}' already exist in tree.")
        # x값이 root의 값보다 큰 경우
        if root.key < x:
            if not root.right:
                root.right = Node(x)
                return True
            return self.insert_working(x,root.right)
        #x값이 root의 값보다 작은 경우
        else:
            if not root.left:
                root.left = Node(x)
                return
            return self.insert_working(x,root.left)

    # 삽입을 비재귀적으로 처리하는 메소드
    def insert_iterative(self,x):
        n = Node(x)
        t = self.root
        while(True):
            if t.key == x:
                raise BST.AlreadyExistException(f"value '{t.key}' already exist in tree.")
            if t.key < x:
                if not t.right:
                    t.right = n
                    break
                t = t.right
            else:
                if not t.left:
                    t.left = n
                    break
                t = t.left
        return True
                
    def delete(self,x):
        # 검사중인 노드
        n = self.root
        # 검사중인 노드의 부모 노드
        parent = None
        # 삭제할 노드가 부모 노드 기준 오른쪽 혹은 왼쪽 원소인지 판별
        parent_right = False
        while True:
            if not n: # 삭제할 요소가 없는 경우
                raise BST.NotExistException(f"value '{x}' not exist")
            if n.key == x: # 삭제할 요소를 찾은 경우
                break
            else:
                parent = n
                # 삭제할 요소가 노드 키값보다 큰 경우
                if n.key < x:
                    parent_right = True
                    n = n.right
                else:
                    parent_right = False
                    n = n.left

        if not n.left: # n이 왼쪽 자식이 없는경우
            if n == self.root:
                self.root = n.right # n이 root이고, 왼쪽 자식이 없는 경우에는 오른쪽 자식을 root로 둔다
            elif parent_right: # 부모 노드 기준 n이 오른쪽 자식이었다면
                parent.right = n.right
            else:
                parent.left = n.right
        elif not n.right: # n이 오른쪽 자식이 없는 경우
            if n == self.root:
                self.root = n.left
            elif parent_right:
                parent.right = n.left
            else:
                parent.left = n.left
        else: # 서브트리에 오른쪽 왼쪽 자식노드가 모두 존재하는 경우이다.
            parent = n
            right = n.right # 오른쪽에서 가장 작은 노드를 검색한다. 가장 작은 노드는 재귀적으로 왼쪽을 더이상 분기할 수 없을때까지 왼쪽으로 분기한다
            parent_right = True # 만약 최초의 서브트리 루트 n의 자식노드의 왼쪽 노드(k라 명시)가 없다면? -> n의 오른쪽 노드를 대체해야 하므로 플래그를 둔다.

            while right.left != None:
                parent = right
                right = right.left
                parent_right = False # 이 반복문이 돈다는 것은 k의 왼쪽 자식 노드에는 최소 한개의 노드가 있다는 것을 의미한다.
            
            n.key = right.key # 오른쪽 서브트리의 가장 작은 값을 n의 값으로 옮긴다.
            if parent_right:
                parent.right = right.right # 결국 parent.right에는 None이 들어가게 된다.
            else:
                parent.left = right.left # 결국 parent.left에는 None이 들어가게 된다.
        
    def dfs(self,root:Node) -> None:
        #검사중인 root가 None인 경우까지 내려간다
        if not root:
            return
        self.dfs(root.left)
        print(f"{root.key}")
        self.dfs(root.right)


    # 이진트리를 출력한다
    def dump(self) -> None:
        self.dfs(self.root)

if __name__ =="__main__":
    b = BST(Node(4))
    
    b.insert(3)
    b.insert(1)
    b.insert_iterative(5)
    b.insert(6)
    b.insert_iterative(2)
    b.dump()
    print("-" * 10)
    b.delete(4)
    b.delete(2)
    b.dump()
