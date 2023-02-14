n = int(input())
ns = list(map(int, input().split()))
ns.sort()
m = int(input())
ms = list(map(int, input().split()))


def bs(start, end, target, arr):
    while end >= start:
        mid = (start+end)//2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            start = mid+1
        else:
            end = mid-1

    return False


for i in ms:
    if bs(0, n-1, i, ns):
        print(1, end=" ")
    else:
        print(0, end=" ")
