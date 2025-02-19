from collections import deque

n, k = map(int, input().split())

dx = [-1, +1, 2]

time = 0

visited = [False] * 100001
visited[n] =True
q = deque([(n, time)])

while q:
    x, time = q.popleft()

    #print(f'x = {x}, time = {time}')

    if x == k:
        print(time)
        break


    for i in range(3):
        if i == 2:
            nx = x * 2
        else:
            nx = x + dx[i]

        if 0<=nx<=100000 and not visited[nx]:
            q.append((nx, time+1))
            visited[nx] = True



