import sys
f = sys.stdin.readline
n = int(f())
arr = [list(f().strip()) for _ in range(n)]


from collections import deque
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def bfs_1(x, y):
    q = deque([(x, y)])
    visited_1[x][y] = True
    color = arr[x][y]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n and not visited_1[nx][ny]:
                if arr[nx][ny] == color:
                    q.append((nx, ny))
                    visited_1[nx][ny] = True

cnt_1 = 0
visited_1 = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited_1[i][j]:
            bfs_1(i, j)
            cnt_1 += 1


def bfs_2(x, y):
    q = deque([(x, y)])
    visited_2[x][y] = True
    color = arr[x][y]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n and not visited_2[nx][ny]:
                if arr[nx][ny] == color:
                    q.append((nx, ny))
                    visited_2[nx][ny] = True

cnt_2 = 0
visited_2 = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            arr[i][j] ='R'

for i in range(n):
    for j in range(n):
        if not visited_2[i][j]:
            bfs_2(i, j)
            cnt_2 += 1

print(cnt_1, cnt_2)