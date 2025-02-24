N = int(input())

ans = [1]
for s in range(2,N+1):
    ans = ans + [s] + ans
print(*ans)