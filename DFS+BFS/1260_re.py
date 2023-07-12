from collections import deque

n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for a in graph:
    a.sort()

visited_dfs = [False] * (n+1)
d_res = []


def dfs(arr, v, visited_dfs):
    visited_dfs[v] = True
    d_res.append(v)

    for i in arr[v]:
        if not visited_dfs[i]:
            dfs(arr, i, visited_dfs)


dfs(graph, k, visited_dfs)


visited_bfs = [False] * (n+1)
b_res = []


def bfs(arr, v, visited_bfs):
    que = deque([v])
    visited_bfs[v] = True

    while que:
        v = que.popleft()
        b_res.append(v)

        for i in arr[v]:
            if not visited_bfs[i]:
                que.append(i)
                visited_bfs[i] = True


bfs(graph, k, visited_bfs)

for i in d_res:
    print(i, end=' ')
print()
for j in b_res:
    print(j, end=' ')
