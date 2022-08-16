n, l = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
tape = data[0] + l
result = 1

for i in range(1, len(data)):
    if data[i] < tape:
        continue
    else:
        tape = data[i]+l
        result += 1

print(result)
