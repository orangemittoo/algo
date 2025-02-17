from collections import defaultdict
N,Q = map(int, input().split())
A = list(map(int, input().split()))
XK = [list(map(int, input().split())) for _ in range(Q)]

dict_map = defaultdict(list)

for i in range(N):
    dict_map[A[i]].append(i + 1)

for x, k in XK:
    if k <= len(dict_map[x]):
        print(dict_map[x][k - 1])
    else:
        print(-1)

