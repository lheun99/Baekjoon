n, m = map(int, input().split())
p, e = [], []

for _ in range(m):
    a, b = map(int, input().split())
    p.append(a)
    e.append(b)

res = 0
while n > 0:
    if n > 6:
        div = 6
    else:
        div = n

    if min(p) <= min(e)*(div):
        res += min(p)
    else:
        res += min(e)*div
    n -= 6

print(res)
