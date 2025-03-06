from collections import deque
import copy, sys
from itertools import combinations as cb

n, m = map(int, sys.stdin.readline().split())
arr = []

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split(' '))))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
#1. 바이러스가 퍼지는 상황 : BFS
def bfs(c_arr):
    q = deque()

    # 바이러스(2) 위치를 찾아서 큐에 추가
    for i in range(n):
        for j in range(m):
            if c_arr[i][j] == 2:
                q.append((i, j))

    while q:
        xx, yy = q.popleft()
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]

            if 0<=nx<n and 0<=ny<m and c_arr[nx][ny] == 0:
                    q.append((nx, ny))
                    c_arr[nx][ny] = 2
    area = sum(row.count(0) for row in c_arr)
    return area

# 2. 벽 세우기 (백 트래킹)
# 벽을 세울 수 있는 모든 경우의 수를 탐색
# 1) 벽은 3개 까지 2) 해당 위치의 값이 0(빈 칸)일 때
def makeWall(cnt):
    if cnt == 3:
        # 연구소 복사본 생성
        c_arr = copy.deepcopy(arr)  
        # 벽 3개가 완성되면 바이러스를 퍼뜨려본다
        answer.append(bfs(c_arr))
        return
    
    for i in range(n):
        for j in range(m):
            # 0(빈 칸)인지 확인
            if arr[i][j] == 0:
                arr[i][j] = 1
                # 두 번째 벽을 세우러 간다
                makeWall(cnt+1)
                # 다시 벽을 허문다 (백트래킹)
                arr[i][j] = 0
                
answer = []

safe = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            safe.append((i, j))
walls = []
for i in cb(safe ,3):
    walls.append(i)

for wall in walls:
    c_arr = copy.deepcopy(arr)
    aa = wall[0]
    bb = wall[1]
    cc = wall[2]

    c_arr[aa[0]][aa[1]] = 1
    c_arr[bb[0]][bb[1]] = 1
    c_arr[cc[0]][cc[1]] = 1

    answer.append(bfs(c_arr))


#makeWall(0)
print(max(answer))