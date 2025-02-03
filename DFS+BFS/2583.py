m, n, k = map(int, input().split())
arr = [[0]*(n) for i in range(m)]


for n in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    w1 = x2 - x1
    h1 = y2 - y1
    w2 = x1 + w1
    h2 = y1 + h1
    for i in range(x1, w2):
        for j in range(y1, h2):
            arr[j][i] = 1

for a in arr:
    print(a)

#상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

