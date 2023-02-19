import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
graph = [[] for i in range(n+1)]
visited = [False]*(n+1)
for i in range(n-1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

dict = {}


def bfs(graph, s, visited):
    que = deque([s])
    visited[s] = True

    while que:
        s = que.popleft()

        for i in graph[s]:
            if not visited[i]:
                dict[i] = s
                que.append(i)
                visited[i] = True


bfs(graph, 1, visited)

for i in range(2, n+1):
    print(dict.get(i))
