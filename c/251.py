N = int(input())

scores = {}
for i in range(N):
    s, t = input().split()
    if s not in scores:
        scores[s] = (int(t), i + 1)
ans = max(scores.values(), key=lambda x: (x[0], -x[1]))
print(ans[1])