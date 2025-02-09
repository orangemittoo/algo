N,S = list(map(int, input().split()))
A_list = list(map(int, input().split()))

ans = 0
for bit in range(1<<N):
    n_sum = 0
    for i in range(N):
        if bit & (1<<i):
            n_sum += A_list[i]
    if n_sum == S:
        ans += 1
print(ans)
