from collections import deque

n, m = map(int, input().split())
mz = [[] for i in range(n)]

for i in range(n):
    line = input()
    for l in line:
        mz[i].append(int(l)) 

#상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(mz):
    que = deque([(0, 0)])

    while que:
        x, y = que.popleft()
 
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0<=nx<n and 0<=ny<m:
                if mz[nx][ny] == 1:
                    que.append((nx,ny))
                    mz[nx][ny] = mz[x][y] + 1
                    

bfs(mz)
print(mz[-1][-1])

for m in mz:
    print(m)
