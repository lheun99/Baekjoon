import sys, copy
from collections import deque

f = sys.stdin.readline
n, m = map(int, f().split())
arr = [list(map(int, f().split())) for i in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# bfs : 바이러스가 퍼진 지도를 만듦
def bfs(c_arr):
    q = deque()
    #바이러스가 시작하는 곳 찾기
    for k in range(n):
        for z in range(m):
            if c_arr[k][z] == 2:
                q.append((k, z))
    
    while q:
        xx, yy = q.popleft()

        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]

            if 0<=nx<n and 0<=ny<m and c_arr[nx][ny] == 0 :
                    q.append((nx, ny))
                    c_arr[nx][ny] = 2
    
    return cnt_safe_zone(c_arr)

# cnt_safe_zone : 안전 영역의 크기 (0의 갯수)
def cnt_safe_zone(c_arr):
    return sum(row.count(0) for row in c_arr)

'''from itertools import combinations as cb
# 1) combinations(조합)을 사용한 벽 3개 세우기
# 벽을 세울 수 있는 곳 0(빈 칸)인 곳 체크
wall = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            wall.append((i, j))

#3개의 조합 만들기
walls = list(cb(wall, 3))

answer = []
#조합별로 벽 세워서 bfs돌리기
for w in walls:
    c_arr = copy.deepcopy(arr)
    one = w[0]
    two = w[1]
    three = w[2]

    c_arr[one[0]][one[1]] = 1
    c_arr[two[0]][two[1]] = 1
    c_arr[three[0]][three[1]] = 1

    answer.append(bfs(c_arr))

print(max(answer))'''

# 2) 백트래킹을 사용한 벽 3개 세우기

answer = []
def wall_back_tracking(cnt):
    if cnt == 3:
        c_arr = copy.deepcopy(arr)
        answer.append(bfs(c_arr))
        
        return 
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall_back_tracking(cnt+1)

                arr[i][j] = 0

wall_back_tracking(0)
print(max(answer))

#백트래킹 최적화는 아직 잘 모르겠음
'''def wall_back_tracking(cnt, start):  # start 인덱스를 추가하여 중복 방지
    global answer
    if cnt == 3:
        c_arr = copy.deepcopy(arr)
        answer = max(answer, bfs(c_arr))  # 최대값 갱신
        return

    for idx in range(start, n * m):  # 1차원 인덱스를 활용해 탐색
        i, j = divmod(idx, m)  # 1차원 인덱스를 (i, j) 좌표로 변환
        if arr[i][j] == 0:
            arr[i][j] = 1
            wall_back_tracking(cnt + 1, idx + 1)  # 중복 방지 위해 start=idx+1
            arr[i][j] = 0  # 백트래킹 (원상 복구)

wall_back_tracking(0, 0)
print(answer)'''