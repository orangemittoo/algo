N = int(input())
A = list(map(int, input().split()))
X = int(input())

S = sum(A)
p = X//S
cnt = p * len(A)
v = p * S
for a in A:
    cnt += 1
    v += a
    if(v > X):
        break

print(cnt)
