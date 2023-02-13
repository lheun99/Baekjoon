from collections import deque
n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


que = deque([1])
visited = [False] * (n+1)
res = []


def bfs(graph, v, visited):
    while que:
        v = que.popleft()
        visited[v] = True
        res.append(v)

        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True


bfs(graph, 1, visited)

print(len(res)-1)
