N = int(input())
L = [list(map(str, input().split())) for _ in range(N)]

ans = set()
for i in range(N):
    ans.add(tuple(L[i]))
print(len(ans))
