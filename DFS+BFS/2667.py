n = int(input())

arr = [list(map(int, input())) for i in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

from collections import deque
def bfs(arr, a, b):
    q = deque([(a, b)])
    arr[a][b] = 0
    cnt = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x+dx[i] 
            ny = y+dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 1:
                    q.append((nx, ny))
                    arr[nx][ny] = 0
                    cnt += 1
    return cnt

answer = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            answer.append(bfs(arr, i, j))

answer.sort()
print(len(answer))
for i in answer:
    print(i)