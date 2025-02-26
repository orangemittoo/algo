N = int(input())
a_list = list(map(int, input().split()))

ans = 0
for i in range(N - 1):
    j = a_list[i]
    if i < j-1 and a_list[j-1] == i + 1:
        ans += 1

x = 0
for i in range(N):
    if a_list[i] == i + 1:
        x += 1

ans += x * (x - 1) // 2

print(ans)