m, n, k = map(int, input().split())
arr = [[0]*(n) for i in range(m)]


for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    w1 = x2 - x1
    h1 = y2 - y1
    w2 = x1 + w1
    h2 = y1 + h1
    for i in range(x1, w2):
        for j in range(y1, h2):
            arr[j][i] = 1

# for a in arr:
#     print(a)

#상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

#bfs

visited_b = [[False]*n for i in range(m)]
from collections import deque
def bfs(arr, x, y, visited_b):
    cnt = 1
    q = deque([(x, y)])
    visited_b[x][y] = True

    while q:
        xx, yy = q.popleft()

        #상하좌우
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]
            
            #네모의 안에 있어야 하고 not visited
            #값이 0이어야 하고
            if 0<=nx<m and 0<=ny<n and not visited_b[nx][ny] :
                if arr[nx][ny] == 0:
                    cnt += 1
                    q.append((nx, ny))
                    visited_b[nx][ny] = True
    return cnt
cnt = 0
res = []
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0 and not visited_b[i][j]:
            cnt += 1
            res.append(bfs(arr, i, j, visited_b))

print(cnt)
res.sort()
for num in res:
    print(num, end=' ')