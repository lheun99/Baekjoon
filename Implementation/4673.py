man = [i for i in range(1, 10000)]


def check(n):
    num = list(map(int, str(n)))
    nums = sum(num) + n

    if nums >= 10000:
        return
    if nums in man:
        man.remove(nums)


for i in range(1, 10000):
    check(i)
for i in man:
    print(i)
