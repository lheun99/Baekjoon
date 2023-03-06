def bs(start, end, target, arr):
    cnt = 0
    while start <= end:
        mid = (start + end)//2
        if arr[mid] < target:
            cnt = mid + 1
            start = mid + 1

        else:
            end = mid - 1

    return cnt


ans = []
t = int(input())
for i in range(t):
    m, n = map(int, input().split())
    ms = list(map(int, input().split()))
    ns = list(map(int, input().split()))
    ns.sort()

    res = 0
    for i in ms:
        res += bs(0, len(ns)-1, i, ns)

    ans.append(res)

for i in ans:
    print(i)
