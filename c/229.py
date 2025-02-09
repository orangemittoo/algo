N, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

sorted_data = sorted(A, key=lambda x: x[0], reverse=True)

ans = 0
used_count = 0
for a, b in sorted_data:
    if(used_count + b <= W):
        ans += a*b
        used_count += b
    else:
        remaining_num = W - used_count
        ans += a*remaining_num
        break

print(ans)