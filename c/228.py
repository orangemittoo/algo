N, K = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(N)]

current_result = [sum(p) for p in P]
comparison_value = sorted(current_result, reverse=True)[K-1]

for score in current_result:
    if score + 300 >= comparison_value:
        print('Yes')
    else:
        print('No')
