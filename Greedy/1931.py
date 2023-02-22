import sys
n = int(sys.stdin.readline().rstrip())
schedule = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    schedule.append((a, b))

schedule.sort(key=lambda x: x[0])
schedule.sort(key=lambda x: x[1])

time = 0
cnt = 0

for s in schedule:
    if s[0] >= time:
        cnt += 1
        time = s[1]

print(cnt)
