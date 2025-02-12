n = int(input())

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

from collections import deque
def bfs(x, y, a, b, l):
    arr = [[0]*l for _ in range(l)]
    visited = [[False]*l for _ in range(l)]

    q = deque([(x, y, 0)])
    visited[x][y] = True

    while q:
        xx, yy, cnt = q.popleft()
        
        if xx == a and yy == b:
                return cnt
        
        for i in range(8):
            nx = xx + dx[i]
            ny = yy + dy[i]
            
            if 0<=nx<l and 0<=ny<l:
                if not visited[nx][ny]:
                    q.append((nx, ny, cnt+1))
                    visited[nx][ny] = True

res = []
for _ in range(n):
    l = int(input())
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    
    res.append(bfs(x, y, a, b, l))
    
for r in res:
    print(r)