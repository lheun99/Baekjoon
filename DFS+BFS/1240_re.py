import sys
from collections import deque

f = sys.stdin.readline

n, m = map(int, f().split())
arr = [[] for _ in range(n+1)]


for _ in range(n-1):
    a, b, c = map(int, f().split())
    arr[a].append((b, c))
    arr[b].append((a, c))
#print(arr)

for _ in range(m):
    start, target = map(int, f().split())
    visited = [False] * (n+1)

    q = deque([(start, 0)])
    visited[start] = True

    while q:
        x, dist = q.popleft()

        if x == target:
            print(dist)
            break

        for i, d in arr[x]:
            if not visited[i]:
                q.append((i, dist + d))
                visited[i] = True