n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

sum = 0
for a, b in zip(A, B):
    sum += (a*b)

print(sum)
