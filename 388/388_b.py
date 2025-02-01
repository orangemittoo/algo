N,D = list(map(int, input().split()))
T_L = [list(map(int, input().split())) for _ in range(N)]


for k in range(1, D + 1):
    max_v = 0
    for i in range(N):
        T, L = T_L[i]
        r = (L + k) * T
        max_v = max(max_v, (L + k) * T)
    print(max_v)