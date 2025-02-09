ii = list(map(int, input().split()))
N = ii[0]
A_list = ii[1:]

ans = []
for bit in range(2**N):
    pattern = []
    for i in range(N):
        if bit & (1<<i):
            pattern.append(A_list[i])
    ans.append(pattern)
print(ans)
