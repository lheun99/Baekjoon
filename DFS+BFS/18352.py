#n, m, k, x = map(int, input().split())
import sys
from collections import deque
f = sys.stdin.readline 

n, m, k, x = map(int, f().split())
arr = [[] for _ in range(n+1)]
visited = [False] * (n+1)
visited[0] = True

for _ in range(m):
    a, b = map(int, f().split())
    arr[a].append(b)

res = []

def bfs(arr, visited, v, k):
    q = deque([(v, 0)])
    visited[v] = True

    while q:
        xx, dis = q.popleft()
        #print(xx, dis)

        if dis == k:
            res.append(xx)

        for j in arr[xx]:
            if not visited[j]:
                visited[j] = True
                q.append((j, dis+1))
                
bfs(arr, visited, x, k)
res.sort()

if len(res) == 0:
    print(-1)

else:
    for r in res:
        print(r)