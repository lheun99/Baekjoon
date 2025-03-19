import sys
from collections import deque
f = sys.stdin.readline

h, w = map(int, f().split())
cheese = [list(map(int, f().split())) for _ in range(h)]

'''for ch in cheese:
    print(ch)'''

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def find_c_bfs():
    c_s = []
    visited = [[False] * w for _ in range(h)]
    q = deque([(0, 0)])
    visited[0][0] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<h and 0<=ny<w and not visited[nx][ny]:
                if cheese[nx][ny] == 1:
                    c_s.append((nx, ny))
                else:
                    q.append((nx, ny))

                visited[nx][ny] = True
    return c_s

time = 0
pieces = 0
while True:
    check_c = find_c_bfs()

    if len(check_c) == 0:
        break

    time += 1
    pieces = len(check_c)

    for i, j in check_c:
        cheese[i][j] = 0

print(time)
print(pieces)
                
