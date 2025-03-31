from collections import deque
import sys
f = sys.stdin.readline

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]


n = int(f())
arr = [[0]*n for _ in range(n)]

a, b, c, d = map(int, f().split())
visited = [[False]*n for _ in range(n)]

q = deque([(a, b, 0)])
visited[a][b] = True

while q:
    x, y, cnt = q.popleft()
    
    if x == c and y == d:
        print(cnt)
        exit()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
            visited[nx][ny] = True
            q.append((nx, ny, cnt+1))
            

print(-1)
