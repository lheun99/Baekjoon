from collections import deque

m, n = map(int, input().split())
arr = []*n

for _ in range(n):
    arr.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

#시작점
q = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i, j, 0))

days = 0
while q:
    x, y, days = q.popleft()

    #max_days = max(max_days, days)  # 최대 날짜 갱신

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<m:
            if arr[nx][ny] == 0:
                q.append((nx, ny, days+1))
                arr[nx][ny] = 1
days = 0
for r in arr:
    if 0 in r:
        print(-1)
        break

    max(max(r), days)

else: 
    print(days)
