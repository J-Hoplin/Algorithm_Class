from __future__ import annotations   
from typing import Any, Type
import hashlib

class Node: # 해시를 구성하는 Node이다.

    def __init__(self,key : Any, value : Any, next)->None:
        self.key = key
        self.value = value
        self.next = next # 다음 해시 Node를 가르킨다.

class ChainedHash:

    def __init__(self,capacity : int) -> None:
        self.capacity = capacity # 해시테이블의 전체 크기
        self.table = [None] * self.capacity # 해시테이블을 리스트로 저장
    
    def hash_value(self,key : Any)-> int: # 해시값을 구한다.
        if isinstance(key, int): # key값이 int형인지 알아본다. 맞으면 True 아니면 False
            return key % self.capacity
        else:
            return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16)%self.capacity) #hexdigest() : 256알고리즘에서 해시값을 16진수 문자열로 꺼낸다.

    def search(self,key : Any) -> Any:
        #입력값의 키가 key값인 원소를 검색해 값 반환 검색 실패시 None반환
        hashValue = self.hash_value(key)
        p = self.table[hashValue]

        while p != None:
            if p.key == key: # 찾고자 하는 키값을 발견할 경우 value반환
                return p.value
            p = p.next # 키가 동이랗지 않은 경우 다음 hash노드 검사
        
        return None # 찾고자 하는 값이 없는 경우에는 None반환
    
    def add(self,key : Any,value : Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]

        while p != None: # 추가하고자 하는 값의 key가 이미 존재하는지에 대한 검사
            if p.key == key: # 추가하고자 하는 값의 key가 이미 있는 경우 추가 불가
                return False
            else:
                p = p.next
        
        newNode = Node(key,value,self.table[hash])
        self.table[hash] = newNode
        return True # 추가가 정상적으로 완료된 경우에는 True반환
    
    def remove(self, key:Any) -> bool:
        hash = self.hash_value(key) # 지우고자 하는 값의 Hash Value를 구한다.
        p = self.table[hash] # 현재노드
        preNode = None # 이전노드

        while p !=None: # 지우고자 하는 값을 찾는다. 
            if p.key == key:
                if preNode == None: # 지우고자 하는 값을 가졌는데 이전 노드가 None인 경우 : 가장 첫번째 노드가 지우고자 하는 경우일때
                    self.table[hash] = p.next
                else: # 지우고자 하는 값을 찾았으며 이전노드가 특정 인스턴스 값을 참조하고있을떄
                    preNode.next = p.next
                return True # 지운 후에 True를 반환 후 종료
            preNode = p 
            p = p.next
        
        return False # 지우고자 하는 값이 존재하지 않는 경우에는 False를 반환한다.
    
    def dump(self) -> None: # 해시 
        for t in range(self.capacity):
            p = self.table[t]
            print(t, end = '')
            while p != None:
                print(f'-> Key : {p.key} Value : {p.value}', end = '')
                p = p.next
            print()