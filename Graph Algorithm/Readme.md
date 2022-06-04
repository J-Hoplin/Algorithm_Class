## BFS,DFS 예시코드에서 사용된 예시 그래프는 아래와 같이 생긴 그래프입니다.

### Copy for Code
```python
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
```
### Picture
![image](https://user-images.githubusercontent.com/45956041/171322831-63f0ece0-c3ea-4f2c-9662-682e7d67dfd9.png)
