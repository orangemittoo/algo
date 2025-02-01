N = int(input())
a = list(map(int, input().split()))

if N == 2:
    print('Yes')
    exit()

ratio = a[1] / a[0]
v = a[0] 

for i in range(N - 1):
    v = v * ratio

print(float(v) == v[len(a)-1])

