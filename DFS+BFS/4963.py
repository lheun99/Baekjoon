#상하좌우, 대각선
dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [1, -1, 0, 0, -1, -1, 1, 1] 

def dfs(arr, x, y, visited):
    #map밖이면 종료
    if x<0 or x>=b or y<0 or y>=a:
        return
    #Sea이거나 방문한 곳이면 종료
    if arr[x][y] == 0 or visited[x][y]:
        return

    visited[x][y] = True

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        #print(f'좌표2 : {nx}, {ny}')   

        #map안에 존재해야 함
        if 0<=nx<b and 0<=ny<a:
            #방문하지 않고 land이어야 함
            if not visited[nx][ny] and arr[nx][ny] == 1:
                dfs(arr, nx, ny, visited)

from collections import deque
def bfs(arr, x, y, visited):
    q = deque([(x, y)])
    visited[x][y] = True
    
    while q:
        xx, yy = q.popleft()
        
        for i in range(8):
            nx = xx + dx[i]
            ny = yy + dy[i]

            #map안에 존재
            if 0<=nx<b and 0<=ny<a:
                #방문하지 않고 land이어야 함
                if not visited[nx][ny] and arr[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = True

res = []
while True:
    a, b = map(int, input().split())
    
    if a==0 and b==0:
        break

    arr = []
    for _ in range(b):
        m = list(map(int, input().split()))
        arr.append(m)

    visited = [[False]*a for _ in range(b)]

    cnt = 0
    for x in range(b):
        for y in range(a):
            if arr[x][y] == 1 and visited[x][y] == False:
                cnt += 1  
                #print(f'좌표 : {x}, {y}')   
                #dfs(arr, x, y, visited)
                bfs(arr, x, y, visited)
    res.append(cnt)

for r in res:
    print(r)
