n = int(input())
nums = list(map(int, input().split()))
nums.sort()

res = 0
for idx in range(n):
    res += nums[idx] * (n-idx)


print(res)
