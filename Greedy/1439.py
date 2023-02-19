import sys
input = sys.stdin.readline().rstrip()

s = input
zeros = s.split("1")
ones = s.split("0")

zero, one = 0, 0

for z in zeros:
    if "0" in z:
        zero += 1
for o in ones:
    if "1" in o:
        one += 1

print(min(zero, one))
