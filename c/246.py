N, K, X = map(int, input().split())
A_list = list(map(int, input().split()))

ans = []
for a in A_list:
    use_k = min(a // X, K)
    K -= use_k
    ans.append(a - use_k * X)

ans.sort(reverse=True)
for i in range(min(len(ans),K)):
    ans[i] = 0
print(sum(ans))