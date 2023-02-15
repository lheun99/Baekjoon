n=int(input())
ns=list(map(int, input().split()))
ns.sort()
m=int(input())
ms=list(map(int, input().split()))

def bs(start, end, target, arr):
    while end >= start:
        mid=(start+end)//2
        
        if arr[mid] == target:
            return dict.get(target)
        elif arr[mid]<target:
            start=mid+1
        else:
            end=mid-1

    return 0

dict={}
for i in ns:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
        
        
for i in ms:
    print(bs(0, n-1, i, ns), end=" ")     