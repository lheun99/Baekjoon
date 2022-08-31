n = int(input())
table = [list(map(int, input().split())) for i in range(n)]
data = []
for weight, height in table:
    cnt = 1
    for oth_weigth, oth_height in table:
        if oth_weigth > weight and oth_height > height:
            cnt += 1
    data.append(str(cnt))

print(" ".join(data))
