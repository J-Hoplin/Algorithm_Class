해시법
===
***

### 해시법이란 ? 

- 해시법(Hashing)은 '데이터를 저장할 위치 = 인덱스'를 간단한 연산으로 구현하는것을 의미한다.

- 해시법을 통해서 원소의 검색, 추가 삭제도 매우 효율적으로 수행할 수 있다.

### 기본적인 용어

- 해시값(Hash Value) : 해시값은 데이터에 접근할떄 기준이 되는 값이다. 원래 입력된 키(Key)값을 해시함수를 이용하여 해싱하여 해시값을 만들어 내는 것이다

- 해시테이블 : 해시값을 인덱스(Index)로 하여 원소를 새로 저장한 배열을 의미한다.

- 해시함수 : Key값을 해시값으로 변환하는 과정을 해시함수(Hash Function)이라고 한다. 해시함수는 단순히 정수간의 산술연산으로도 구현할 수 있지만 hashlib의 md5() 혹은 sha256()을 사용하여 구현할 수 도 있다.

- 버킷 : 해시테이블에서 만들어진 원소를 버킷이라고 한다.

### 해시충돌

- 이 상황을 가정하자. 사용자가 10이라는 키값을 가진 한 value를 넣으려 한다고 가정하자. key값을 해싱하여 넣으려는 데 같은 값의 해시값을 가진 버킷이 존재한다. 이와 같이 버킷값이 중복되는 현상을 **'충돌'**이라고 한다.

### 해시충돌에 대한 대응법 두가지

- [체인법](https://github.com/J-hoplin1/Problem-Solving/blob/master/Study%20D.S%20and%20Algorithms/Python/Hash/ChainingHash.py) : 해시값이 같은 원소들끼리 Linked List로 구현한다. Open Hashing이라고도 부른다

- [오픈주소법](https://github.com/J-hoplin1/Problem-Solving/blob/master/Study%20D.S%20and%20Algorithms/Python/Hash/openAddressHash.py) : 빈 버킷을 찾을때까지 해시값을 다시 구한다. Close Hashing이라고도 부른다.

### 해시 알고리즘 구현시에 사용하는 Hashlib의 주 메소드

- [sha256()](https://ko.wikipedia.org/wiki/SHA) : sha256은 RSA의 FIPS알고리즘을 바탕으로 하며 주어진 바이트문자열이 해시값을 구하는 해시알고리즘의 생성자다. 

- md5() : 128비트 암호화 해시함수이다.

- encode()함수 : hashlib의 sha256()은 바이트 문자열의 인수를 전달해야한다. 그래서 key값을 str()형태로 형변환한 후 그 문자열을 encode()함수에 전달하여 바이트 문자열을 생성한다.

- hexdigest()함수 : sha256()알고리즘에서 해시값을 16진수 문자열로 꺼낸다.
