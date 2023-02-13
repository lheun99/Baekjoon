n = int(input())
words = [input() for i in range(n)]
word = list(set(words))
word.sort(key=lambda x: (len(x), x))
for w in word:
    print(w)
