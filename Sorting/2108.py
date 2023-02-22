import sys
from collections import Counter
n=int(sys.stdin.readline().rstrip())
nums=[int(sys.stdin.readline().rstrip()) for i in range(n)]
res=[]

nums.sort()
print(round(sum(nums)/len(nums)))


print(nums[n//2])

cnt = Counter(nums).most_common()
cnts = sorted(cnt, key=lambda x: (-x[1], x[0]))

if n == 1:
    print(nums[0])
elif cnts[0][1] == cnts[1][1]:
    print(cnts[1][0])
else:
    print(cnts[0][0])
    
print(max(nums) - min(nums))