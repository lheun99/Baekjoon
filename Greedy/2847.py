n = int(input())
data = [int(input()) for i in range(n)]

max_num = data[-1]
result = 0

for i in range(n-1, 0, -1):
    if data[i-1] >= data[i]:
        result += data[i-1] - (data[i]-1)
        data[i-1] = data[i]-1
    else:
        continue

print(result)
