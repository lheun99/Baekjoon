import sys
from collections import deque

f = sys.stdin.readline

n, m = map(int, f().split())

arr = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, f().split())
    arr[a].append((b, c))
    arr[b].append((a, c))


def bfs(start, target):
    visited = [False] * (n+1)

    # 현재노드, 누적거리
    q = deque([(start, 0)]) 
    visited[start] = True

    while q:
        x, dist = q.popleft()
        # 목표 노드 도착 시 종료
        if x == target:
            return dist
        
        for nx, d in arr[x]:
            if not visited[nx]:
                q.append((nx, dist+d))
                visited[nx] = True

for _ in range(m):
    xx, yy = map(int, f().split())
    print(bfs(xx, yy))