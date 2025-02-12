n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

#2차원 배열을 구성하고 있는 숫자 리스트
nums = list(set(num for row in arr for num in row))
max_n = max(nums)
min_n = min(nums)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
from collections import deque
def bfs(arr, x, y, visited, h):
    q = deque([(x, y)])
    visited[x][y] = True

    while q:
        xx, yy = q.popleft()
        
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]
            
            #map 범위 안이어야 함
            if 0<=nx<n and 0<=ny<n:
                #h(높이) 초과이어야 함 & 방문하지 않아야 함
                if arr[nx][ny] > h and visited[nx][ny] == False:
                    #print(f'nx = {nx} ny = {ny} h = {h}')
                    q.append((nx, ny))
                    visited[nx][ny] = True

res = []


for h in range(min_n-1, max_n+1):
    #print(h)
    visited = [[False]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
                #방문하지 않은 곳 & h(높이) 초과이어야 함
                if not visited[i][j] and arr[i][j] > h:
                    cnt += 1
                    bfs(arr, i, j, visited, h)
    res.append(cnt)

    
print(max(res))