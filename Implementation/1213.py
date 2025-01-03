import sys
data = sys.stdin.readline().rstrip()

dict = {}
for i in data:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

one = 1
one_al = ""
pal = ""
for j in dict:
    if dict[j] % 2 != 0:
        one += 1
        one_al = j
    else:
        pal += j

if one != 1:
    print("I'm Sorry Hansoo")
else:
    print(pal + one_al + pal[::-1])