N, M = list(map(int, input().split()))
A = [list(input()) for _ in range(N*2)]

scores = [0] * (2*N)
order = list(range(2*N))

def judge(l, r):
    if (l == 'G' and r == 'C') or (l == 'C' and r == 'P') or (l == 'P' and r == 'G'):
        return 1
    if (r == 'G' and l == 'C') or (r == 'C' and l == 'P') or (r == 'P' and l == 'G'):
        return -1
    return 0

for i in range(M):
    for k in range(N):
        p1, p2 = order[2*k], order[2*k+1]
        result = judge(A[p1][i], A[p2][i])
        if result == 1:
            scores[p1] += 1
        elif result == -1:
            scores[p2] += 1
    order.sort(key=lambda x: (-scores[x], x))
for i in order:
    print(i + 1)