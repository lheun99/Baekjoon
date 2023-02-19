n = int(input())
words = [input() for i in range(n)]
cnt = 0

for w in words:
    gc=[]
    for idx in range(1, len(w)):
        if w[idx-1] == w[idx]:
            continue
        elif w[idx] in gc: 
            cnt += 1
            break
        elif w[idx-1] != w[idx]:
            gc.append(w[idx-1])
            
print(n-cnt)