t = int(input())
result = []

for i in range(t):
    data = ""
    r, s = input().split()
    for j in s:
        data += j*int(r)

    print(data)
