from collections import deque
import sys

# 빠른 입력 필요
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited = [False] * (n+1)

"""
-> dfs로 처리 시, Recursion Error 발생
def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
"""


def bfs(graph, v, visited):
    que = deque([v])
    visited[v] = True

    while que:
        v = que.popleft()

        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True


cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        bfs(graph, i, visited)
        cnt += 1
    else:
        continue

print(cnt)
