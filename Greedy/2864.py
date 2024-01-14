A, B = input().split()
a = [A]
b = [B]

if "5" in A:
    a.append(A.replace("5", "6"))

if "6" in A:
    a.append(A.replace("6", "5"))

if "5" in B:
    b.append(B.replace("5", "6"))

if "6" in B:
    b.append(B.replace("6", "5"))

print(int(min(a)) + int(min(b)), end=" ")
print(int(max(a)) + int(max(b)))
