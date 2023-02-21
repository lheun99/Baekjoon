from collections import deque

n=int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int, input())))
visited=[[False for i in range(n)] for j in range(n)]

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

def bfs(a, b, graph, visited):
    que=deque()
    que.append((a, b))
    visited[a][b] = True
    cnt = 1
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            elif graph[nx][ny] == 1 and not visited[nx][ny]:
                cnt += 1
                que.append((nx, ny))
                visited[nx][ny] = True
    return cnt

 
res = []
for a in range(n):
    for b in range(n):
        if graph[a][b] == 1 and not visited[a][b]:
            res.append(bfs(a, b, graph, visited))
res.sort()          
print(len(res))   
for i in res:
    print(i)