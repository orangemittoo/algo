N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

center = N // 2
sum_total = 0

for i in range(N):
    for j in range(N):
        required_stones = (N+1)//2 - max(abs(center - i), abs(center - j))
        sum_total += S[i][j] - required_stones

print(sum_total)
