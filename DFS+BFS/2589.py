from collections import deque

h, w = map(int, input().split())
arr = [[] for _ in range(h)]

for i in range(h):
    for j in input():
        arr[i].append(j)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def bfs(arr, x, y, cnt):
    visited = [[False]*w for vv in range(h)] 
    q = deque([(x, y, cnt)])
    visited[x][y] = True

    while q:
        xx, yy, cnt = q.popleft()
        #print(f"({xx}, {yy})")
        for ii in range(4):
            nx = xx + dx[ii]
            ny = yy + dy[ii]

            if 0<=nx<h and 0<=ny<w and not visited[nx][ny]:
                if arr[nx][ny] == 'L':
                    q.append((nx, ny, cnt+1))
                    visited[nx][ny] = True
    
    return cnt

res = 0
for a in range(h):
    for b in range(w):
        if arr[a][b] == 'L':
            #print(f'({a}, {b})')
            cnt = bfs(arr, a, b, 0)
            res = max(res, cnt)

print(res)