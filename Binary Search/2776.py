t = int(input())


def bs(start, end, target, arr):
    while end >= start:
        mid = (start+end)//2

        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            end = mid-1
        else:
            start = mid+1

    return 0


for i in range(t):
    n = int(input())
    ns = list(map(int, input().split()))
    ns.sort()
    m = int(input())
    ms = list(map(int, input().split()))

    for j in ms:
        print(bs(0, n-1, j, ns))
