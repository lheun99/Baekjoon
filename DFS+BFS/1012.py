from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a, b, graph, visited):
    que = deque()
    que.append((a, b))
    visited[a][b] = True
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            elif graph[nx][ny] == 1 and not visited[nx][ny]:
                que.append((nx, ny))
                visited[nx][ny] = True
    return


t = int(input())
res = []
for i in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for j in range(n)]
    visited = [[False] * m for j in range(n)]
    for j in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    cnt = 0
    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1 and not visited[a][b]:
                bfs(a, b, graph, visited)
                cnt += 1
    res.append(cnt)
for i in res:
    print(i)
