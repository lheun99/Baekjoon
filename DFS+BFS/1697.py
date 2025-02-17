n, k = map(int, input().split())

dx = [-1, +1, 2]

time = 0

from collections import deque
q = deque([(n, time)])

for z in range(5):
    x, time = q.popleft()

    if x < k:
        nx = x
        for i in range(3):
            if dx[i] == 2:
                nx = x * 2
            else:
                nx = x + dx[i]
            
            q.append((nx, time+1))
    else:
        break

print(time)
