import sys
from collections import deque
f = sys.stdin.readline

n, m = map(int, f().split())
arr = [list(map(int, f().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#녹는 빙산
def melt(icebergs):
    # 높이 감소를 한 번에 처리하기 위해 따로 저장
    melt_amount = [[0]*m for _ in range(n)]

    for x, y in icebergs:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if arr[nx][ny] == 0:
                    melt_amount[x][y] += 1

    new_icebergs = []
    for x, y in icebergs:
        arr[x][y] = max(0, arr[x][y] - melt_amount[x][y])
        if arr[x][y] > 0:
            new_icebergs.append((x, y))
    return new_icebergs

#덩어리 확인
def count_chunks(icebergs, visited):
    cnt = 0
    for x, y in icebergs:
        if not visited[x][y]:
            cnt += 1
            
            q = deque([(x, y)])
            visited[x][y] = True

            while q:
                xx, yy = q.popleft()

                for i in range(4):
                    nx = xx + dx[i]
                    ny = yy + dy[i]

                    if 0<=nx<n and 0<=ny<m:
                        if not visited[nx][ny] and arr[nx][ny] > 0:
                            visited[nx][ny] = True
                            q.append((nx, ny))
    return cnt

time = 0
#빙산 체크
icebergs = []
for i in range(n):
    for j in range(m):
        if arr[i][j] > 0:
            icebergs.append((i, j))
                         
while True:
    visited = [[False]*m for _ in range(n)]
    chunk_count = count_chunks(icebergs, visited)

    if chunk_count >= 2:
        print(time)
        break
    
    if not icebergs:  # 모두 녹음
        print(0)
        break

    icebergs = melt(icebergs)
    time += 1