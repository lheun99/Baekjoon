from collections import deque
n, m, k = map(int, input().split())
arr = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for a in arr:
    a.sort()

visited_d = [False]*(n+1)
d_res = []


def dfs(graph, v, visited_d):
    visited_d[v] = True
    d_res.append(v)

    for i in graph[v]:
        if not visited_d[i]:
            dfs(graph, i, visited_d)


dfs(arr, k, visited_d)


visited_b = [False]*(n+1)
b_res = []


def bfs(graph, v, visited_b):
    que = deque([v])
    visited_b[v] = True

    while que:
        v = que.popleft()
        b_res.append(v)

        for i in graph[v]:
            if not visited_b[i]:
                que.append(i)
                visited_b[i] = True


bfs(arr, k, visited_b)

for i in d_res:
    print(i, end=" ")
print()
for j in b_res:
    print(j, end=" ")
