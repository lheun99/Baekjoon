## DFS/BFS

### 스택

### 큐

- 파이썬에서 큐 구현 시에는 **collections모듈에서 제공하는 deque 자료구조를 활용**한다
- 리스트보다 데이터를 넣고 빼는 속도가 효율적이다

```python
from collections import deque
que = deque()

que.append()
que.appendleft()

que.pop()
que.left()

que.reverse()

```

### 재귀함수

---

### 1. DFS

- **그래프를 표현하는 2가지 방식**

  - 인접 행렬 (Matrix) : 2차원 배열로 그래프의 연결 관계를 표현하는 방식
  - 인접 리스트 (List) : 리스트로 그래프의 연결 관계를 표현하는 방식

- **인접 행렬**
  ```python
  INF = 999999999
  graph = [
      [0, 7, 5],
      [7, 0, INF],
      [5, INF, 0]
  ]
  ```
- **인접 리스트**

  ```python
  graph = [[] for _ in range(3)]

  graph[0].append((1, 7))
  graph[0].append((2, 5))

  graph[1].append((0, 7))

  graph[2].append((0, 5))
  ```

  - 인접 행렬 방식은 노드 개수가 많을 수록 메모리 낭비, 앞에서부터 차례대로 확인해야

  - **특정한 노드와 연결된 모든 인접 노드를 순회해야 하는 경우, 인접 리스트 방식 사용**

- **DFS는 스택 자료구조를 이용한다**
- _O(N)_

### 1-1. DFS 예제 (재귀)

```python
#DFS메서드 정의
def dfs(graph, v, visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')

#현재 노드와 연결된 다른 노드를 재귀적으로 방문
for i in graph[v]:
    if not visited[i]:
        dfs(graph, i, visited[i])

#각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [[~]]

#각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited = [False]*9

#정의된 DFS 함수 호출
dfs(graph, 1, visited)
```

---

### 2. BFS

- **BFS는 큐 자료구조를 이용한다**
- _O(N)_
- DFS보다 일반적으로 실제 수행 시간이 좋은 편이다

### 2-1. BFS 예제

```python
from collections import deque

#BFS 메서드 정의
def bfs(graph, start, visited):
    #큐(Queue) 구현을 위해 deque 라이브러리 사용
    que = deque([start])

    #현재 노드를 방문 처리
    visited[start] = True

    #큐가 빌 때까지 반복
    while que:
        #큐에서 하나의 원소를 뽑아 출력
        v = que.popleft()
        print(v, end=' ')

        #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True

#각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [[~]]

#각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited = [False]*9

#정의된 DFS 함수 호출
bfs(graph, 1, visited)
```
