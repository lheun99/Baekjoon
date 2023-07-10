n = int(input())

for i in range(n):
    VPS = input()
    stack = []

    for v in VPS:
        if v == "(":
            stack.append(v)
        elif v == ")":
            if len(stack) == 0:
                stack.append(v)
                break
            else:
                stack.pop()

    if len(stack) == 0:
        print("YES")

    else:
        print("NO")
