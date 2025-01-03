from collections import deque

n, m, k = map(int, input().split())

arr = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for a in arr:
    a.sort()

visited_d = [False] * (n+1)
visited_b = [False] * (n+1)

dfs_an = []
def dfs(arr, v, visited_d):
    visited_d[v] = True
    dfs_an.append(v)

    for i in arr[v]:
        if not visited_d[i]:
            dfs(arr, i, visited_d)

dfs(arr, k, visited_d)

bfs_an = []
def bfs(arr, v, visited):
    que = deque([v])
    visited[v] = True

    while que:
        v = que.popleft()
        bfs_an.append(v)

        for i in arr[v]:
            if not visited_b[i]:
                que.append(i)
                visited_b[i] = True

bfs(arr, k, visited_b)

print(dfs_an)
print(bfs_an)