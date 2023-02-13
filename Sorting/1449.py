n, l = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

tape = nums[0] + l
res = 1

for idx in range(1, len(nums)):
    if tape > nums[idx]:
        continue
    else:
        tape = nums[idx] + l
        res += 1

print(res)
