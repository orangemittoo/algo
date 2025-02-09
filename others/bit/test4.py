N = int(input())
A_list = list(map(int, input().split()))

ans = float('inf')
for bit in range(1<<N):
    sum1 = 0
    sum2 = 0
    for i in range(N):
        if bit & (1<<i):
            sum1 += A_list[i]
        else:
            sum2 += A_list[i]
    ans = min(ans, abs(sum1 - sum2))
    
print(ans)
