N = list(input())
n = len(N)
ans = 0

for i in range(2**n):
    left = []
    right = []

    for j in range(n):
        if (i >> j) & 1:
            left.append(N[j])
        else:
            right.append(N[j])

    left.sort(reverse=True) 
    right.sort(reverse=True)

    if len(left) == 0 or len(right) == 0:
        continue

    if left[0] == '0' or right[0] == '0':
        continue

    ans = max(ans, int(''.join(left)) * int(''.join(right)))

print(ans)
