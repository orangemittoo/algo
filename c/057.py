import math
N = int(input())

ans = float('inf')
for i in range(1, int(math.sqrt(N)) + 1):
    if N % i == 0:
        a, b = i, N//i
        ans = min(ans, max(len(str(a)), len(str(b))))

print(ans)