n = int(input())
sum = 0
cnt = 0

while True:
    cnt += 1
    sum += cnt
    if sum > n:
        break
print(cnt - 1)
