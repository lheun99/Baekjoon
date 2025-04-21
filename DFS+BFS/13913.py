import sys
from collections import deque
f = sys.stdin.readline

n, k = map(int, f().split())
MAX = 100001

dx = [-1, 1]
visited = [False] * MAX
prev = [-1] * MAX #이전 위치 저장용

def bfs():
    q = deque([(n, 0)])
    visited[n] = True

    while q:
        x, c = q.popleft()

        if x == k:
            return c
        
        for nx in (x-1, x+1, x*2):
            if 0<= nx < MAX and not visited[nx]:
                visited[nx] = True
                prev[nx] = x #nx는 x에서 왔다
                q.append((nx, c+1))

cnt = bfs()

#경로 복원
path = []
cur = k

while cur != -1:
    path.append(cur)
    cur = prev[cur]

path.reverse()

#print(len(path)-1)
print(cnt)
print(' '.join(map(str, path)))