import bisect
N,M = list(map(int,input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A = sorted(A)
B = sorted(B)

ans = []
for a in A:
    b = bisect.bisect(B,a)
    if b == 0:
        # Bの最小値より低い
        ans.append(B[0] - a)
    elif b == M:
        # Bの最大値より高い
        ans.append(a - B[-1])
    else:
        # どれかの間
        if a == B[b]:
            ans.append(0)
        else:
            ans.append(B[b] - a)
            ans.append(a - B[b-1])

print(min(ans))