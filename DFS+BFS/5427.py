import sys
from collections import deque
f = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def bfs(arr, a, b, fire_q):
    visited = [[False]*w for _ in range(h)]
    visited[a][b] = True
    q = deque([(a, b, 0)])
    
    while q:
        # 불 확산
        for _ in range(len(fire_q)):
            fx, fy = fire_q.popleft()
            for f_idx in range(4):
                f_nx = fx + dx[f_idx]
                f_ny = fy + dy[f_idx]
    
                if 0<=f_nx<h and 0<=f_ny<w:
                    if arr[f_nx][f_ny] == '.':
                        # 불 확산
                        arr[f_nx][f_ny] = '*'
                        fire_q.append((f_nx, f_ny))


        # 상근 탈출
        for _ in range(len(q)):
            x, y, time = q.popleft()
            # 탈출조건
            if x == 0 or x == h-1 or y == 0 or y == w-1:
                return time + 1
            
            for idx in range(4):
                nx = x + dx[idx]
                ny = y + dy[idx]
    
                if 0<=nx<h and 0<=ny<w:
                    if arr[nx][ny] == '.' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny, time+1))

    return "IMPOSSIBLE"

n = int(f())
result = 0
for _ in range(n):
    w, h = map(int, f().split())

    arr = [list(f().strip()) for _ in range(h)]

    # 불 위치 확인
    fire_q = deque()
    for a in range(h):
        for b in range(w):
            if arr[a][b] == "*":
                fire_q.append((a, b))
 

    for a in range(h):
        for b in range(w):
            if arr[a][b] == "@":
                result = bfs(arr, a, b, fire_q)
    
    print(result)



