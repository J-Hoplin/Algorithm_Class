from typing import Any, Type
from enum import Enum
import hashlib

class status(Enum): # 각 버킷 상태에 대한 속성을 부여한다. 속성값들을 열거형 클래스를 상속받아 구현
    OCCUPIED = 0
    EMPTY = 1
    DELETED = 2

class Bucket(object):

    #버킷 초기화
    def __init__(self,key : Any = None, value : Any = None, stat : status = status.EMPTY) -> None: #각 파라미터 값에 초기값을 초기화한다.
        self.key = key
        self.value = value
        self.stat = stat
    
    # 값을 집어넣을때 사용하는 메소드
    def setValue(self, key : Any, value : Any, stat : status) -> None:

        self.key = key
        self.value = value
        self.stat = stat
    
    # 버킷의 속성 변경이 있을떄 속성을 변경하는 메소드
    def setStatus(self, stat : status) -> None:

        self.stat = stat

#개방 주소(오픈 해싱)법으로 구현한 해시
class OpenAddress(object):
    def __init__(self,capacity : int):
        self.capacity = capacity
        self.hashtable = [Bucket()] * self.capacity


    def hashValue(self, key : Any) -> int:
        if isinstance(key, int): # 입력된 키값의 자료형이 int class인 경우
            return key % self.capacity
        else: # 입력된 키가 문자열 혹은 다른 타입인 경우
            return (int(hashlib.md5(str(key).encode()).hexdigest(),16) % self.capacity)
    
    def rehashValue(self,key : Any) -> int:
        return (self.hashValue(key) + 1) % self.capacity # 개방 주소 해시법이므로 버킷이 비어있을때 까지 계속해서 재해싱(rehashing)을 반복해 준다.

    #찾고자 하는 키값이 들은 '노드'를 반환하는 메소드
    def searchNode(self, key) -> Any:
        hashVal = self.hashValue(key) # 찾고자하는 키값의 해시값 반환
        p = self.hashtable[hashVal]

        for a in range(self.capacity):
            if p.stat == status.EMPTY:
                break # 속성이 비어있는거로 설정되어있는경우 값이 애초에 저장되지 않았던것이기에 반복문 중단
            elif p.stat ==status.OCCUPIED and p.key == key:
                return p
            else:
                hashVal = self.rehashValue(hashVal)
                p = self.hashtable[hashVal]
        return None # 찾고자 하는 값이 없는 경우에는 None을 반환한다.
    
    def search(self, key):
        p = self.searchNode(key)
        if not p: # 찾고자 하는 값이 없는 경우에
            return None
        else:# 찾고자 하는 값이 존재하는 경우에
            return p.value
    
    def add(self,key : Any,value : Any) -> bool: # bool : 해시테이블에 값 추가 성공하였는지 실패하였는지에 대한 boolean타입
        if self.search(key): # 추가하고자 하는 key값이 이미 존재하는 경우에 
            return False
        else:
            hashVal = self.hashValue(key) # 우선 주어진 키에 대한 해시값을 구하고
            p = self.hashtable[hashVal] # 해당 해시값에 대한 hash테이블의 index노드를 우선 포인팅한다.
            for a in range(self.capacity):
                if p.stat == status.EMPTY or p.stat == status.DELETED: # 지정한 노드의 속성이 비어있거나 값이 지워진 상태인 경우
                    self.hashtable[hashVal] = Bucket(key,value,status.OCCUPIED)
                    return True # 값을 저장하고 True반환
                else:
                    hashVal = self.rehashValue(hashVal) # 이미 다른 값이 있는 경우에는 비어있는 버킷을 찾을때까지 재해싱
                    p = self.hashtable[hashVal]
            return False
    
    def remove(self,key : Any) -> bool:
        p = self.searchNode(key)
        if not p:
            return False
        else:
            p.setStatus(status.DELETED)
            return True
    
    def dump(self):
        for a in range(self.capacity):
            print(f'{a : 2}', end = '   ')
            if self.hashtable[a].stat == status.OCCUPIED:
                print(f'Key : {self.hashtable[a].key} / Value : {self.hashtable[a].value}')
            elif self.hashtable[a].stat == status.DELETED:
                print("삭제된 상태")
            else:
                print("아무 값도 등록되지 않음.")