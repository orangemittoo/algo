A, B, C, X, Y = map(int, input().split())
ans = float('inf')

for i in range(0, max(X, Y) + 1):
    sum_c = i * C * 2
    sum_ab = A * max(0, X - i) + B * max(0, Y - i)
    ans = min(ans, sum_ab + sum_c)

print(ans)