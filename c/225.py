N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]

start_pos = B[0][0]
start_i = (start_pos - 1) // 7
start_j = (start_pos - 1) % 7

if start_j + M > 7:
    print('No')
    exit()

for y in range(N):
    for x in range(M):
        expected_value = (start_i + y) * 7 + (start_j + x + 1)
        if B[y][x] != expected_value:
            print('No')
            exit()

print('Yes')