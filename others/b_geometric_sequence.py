N = int(input())
a = list(map(int, input().split()))

for i in range(1, N - 1):
    if a[i + 1] * a[0] != a[1] * a[i]:
        print('No')
        exit()

print('Yes')