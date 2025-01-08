from collections import deque

n = int(input())
arr = [[] for i in range(n+1)]


a, b = map(int, input().split())
m = int(input())

for i in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

visited_d = [False] * (n+1)
res_d = []
def dfs(arr, v, visited_d, num):
    visited_d[v] =True

    if v == b:
        res_d.append(num)
    for i in arr[v]:
        if not visited_d[i]:
            dfs(arr, i, visited_d, num+1)

dfs(arr, a, visited_d, 0)

visited_b = [False] * (n+1)
res_b = []
from collections import deque
def bfs(arr, v, visited_b, num):
    que = deque([(v, 0)]) # (노드, 깊이)
    visited_b[v] = True

    while que:
        v, num = que.popleft()
        if v == b:
            res_b.append(num)

        for i in arr[v]:
            if not visited_b[i]:
                que.append((i, num+1))
                visited_b[i] = True

bfs(arr, a, visited_b, 0)

if len(res_b) == 0:
    print(-1)
else:
    print(res_b[0])