import sys
from collections import deque

f = sys.stdin.readline
F, S, G, U, D = map(int, f().split())

def bfs(cnt):
    q = deque([(S, cnt)])
    visited[S] = True

    while q:
        x, c = q.popleft()

        if x == G:
            print(c)
            return
        
        for i in ('U', 'D'):
            if i == 'U':
                nx = x + U
            elif i == 'D':
                nx = x - D
            
            if 0 < nx <= F and not visited[nx]:
                q.append((nx, c + 1))
                visited[nx] = True

    
    print("use the stairs")

visited = [False] * (F+1)
cnt = 0
bfs(cnt)