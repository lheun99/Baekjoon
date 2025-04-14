import sys
from collections import deque

f = sys.stdin.readline

dz = [0, 0, 0, 0, 1, -1]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0 , 1, -1, 0, 0]
def bfs(arr, visited, e, f, g):

    q = deque([(e, f, g, 0)])
    visited[e][f][g] = True

    while q:
        z, x, y, time = q.popleft()

        if arr[z][x][y] == "E":
            print(f'Escaped in {time} minute(s).')
            return 

        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nz<l and 0<=nx<r and 0<=ny<c:
                if arr[nz][nx][ny] in ('.', 'E') and not visited[nz][nx][ny]:
                   q.append((nz, nx, ny, time+1))
                   visited[nz][nx][ny] = True
    
    print("Trapped!")

while True:
    line = f()
    if not line:
        continue
    if line.strip() == '':
        continue

    l, r, c = map(int, line.split())
    
    if l == 0 and r == 0 and c == 0:
        break

    arr = []
    for j in range(l):
        floor = []
        while len(floor) < r:
            line = f().strip()
            if not line:
                continue
            floor.append(list(line))
        arr.append(floor)
    
    visited = [[[False]*c for _ in range(r)] for _ in range(l)]
    
    for z in range(l):
        for x in range(r):
            for y in range(c):
                if arr[z][x][y] == 'S':
                    bfs(arr, visited, z, x, y)