k = int(input())
arr = []

for i in range(k):
    data = int(input())

    if data == 0:
        arr.pop()

    else:
        arr.append(data)

if len(arr) == 0:
    print(0)
else:
    print(sum(arr))
