N = int(input())
A_list = list(map(int, input().split()))

ans = 0
for bit in range(1<<N):
    n = 0
    for i in range(N):
        if bit & (1<<i):
            n ^= A_list[i]
    ans = max(ans, n)
print(ans)
