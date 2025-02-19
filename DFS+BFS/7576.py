from collections import deque

m, n = map(int,input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

q = deque()

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i, j, 0))

max_d = 0
while q:
    x, y, day = q.popleft()
    max_d = max(max_d, day)
    #print(x, y, day)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<m:
            if arr[nx][ny] == 0:
                q.append((nx, ny, day+1))
                arr[nx][ny] = 1

for row in arr:
    if 0 in row:
        print(-1)
        exit(0)
print(max_d)

##