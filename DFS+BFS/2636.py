import sys
from collections import deque

f = sys.stdin.readline

h, w = map(int, f().split())

cheese = [list(map(int, f().split())) for _ in range(h)]

#녹을 치즈(c)리스트 찾기 (bfs)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def melt_list_bfs():
    q = deque([(0, 0)])
    visited = [[False] * w for _ in range(h)]
    visited[0][0] = True

    be_c = []

    while q:
        xx, yy = q.popleft()
        
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]

            if 0<=nx<h and 0<=ny<w and not visited[nx][ny]:
                visited[nx][ny] = True

                if cheese[nx][ny] == 1:
                    #접촉된 부분 > 녹을 치즈(c)
                    be_c.append((nx, ny))
                else:
                    #외부공기(0) 탐색
                    q.append((nx, ny))

        
    return be_c

last_cheese = 0
time = 0
while True: 
    # 외부공기(0)를 탐색해서 녹을 치즈(c) 
    melt_list = melt_list_bfs()
    
    # 더 이상 녹을 부분이 없다면 종료
    if not melt_list:
        break

    # 남은 치즈 조각
    last_cheese = len(melt_list)
    
    #녹을 치즈(c) 부분 녹이기
    for x, y in melt_list:
        #print(x, y)
        cheese[x][y] = 0
    
    time += 1

print(time)
print(last_cheese)
