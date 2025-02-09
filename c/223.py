N = int(input())
input_list = [list(map(int, input().split())) for _ in range(N)]

total_time = 0
for i in range(N):
    a,b = input_list[i]
    total_time += a/b
half_time = total_time / 2

current_time = 0
current_length = 0

for i in range(N):
    a,b = input_list[i]
    burn_time = a/b

    if current_time + burn_time > half_time:
        remaining_time = half_time - current_time
        current_length += b * remaining_time
        break

    current_time += burn_time
    current_length += a

print(current_length)