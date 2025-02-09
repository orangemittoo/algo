N = int(input())
S = list(input())

next_pos = [[-1] * 10 for _ in range(N+1)]

for d in range(10):
    next_pos[N][d] = -1

for i in range(N-1, -1, -1):
    for d in range(10):
        next_pos[i][d] = next_pos[i+1][d]
    current_digit = int(S[i])
    next_pos[i][current_digit] = i

count = 0
for num in range(1000):
    d1 = num // 100
    d2 = (num //10) % 10
    d3 = num % 10
    
    idx1 = next_pos[0][d1]
    if idx1 == -1:
        continue
    idx2 = next_pos[idx1+1][d2]
    if idx2 == -1:
        continue
    idx3 = next_pos[idx2+1][d3]
    if idx3 == -1:
        continue

    count += 1

print(count)