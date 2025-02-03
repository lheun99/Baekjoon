n, m, v = map(int, input().split())

arr = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in arr:
    i.sort()

# dfs코드
visited_d = [False] * (n+1)
def dfs(arr, visited_d, v):
    print(v, end=' ')
    visited_d[v] = True

    for i in arr[v]:
        if not visited_d[i]:
            dfs(arr, visited_d, i)
dfs(arr, visited_d, v)

print()

# bfs코드
visited_b = [False] * (n+1)
from collections import deque
def bfs(arr, visited_b, v):
    q = deque([v])
    visited_b[v] = True

    while q:
        a = q.popleft()
        print(a, end=' ')
        for i in arr[a]:
            if not visited_b[i]:
                q.append(i)
                visited_b[i] = True
bfs(arr, visited_b, v)