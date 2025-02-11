N,M,Q = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(Q)]

sum_list = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(N):
    for j in range(M):
        sum_list[i+1][j+1] = A[i][j] + sum_list[i][j+1] + sum_list[i+1][j] - sum_list[i][j]

for a,b,c,d in B:
    a, b, c, d = a + 1, b + 1, c + 1, d + 1 
    print(sum_list[c][d] - sum_list[a-1][d] - sum_list[c][b-1] + sum_list[a-1][b-1])