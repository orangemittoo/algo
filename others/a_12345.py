a = list(map(int, input().split()))

sorted_a = sorted(a)
for i in range(len(a) - 1):
    a[i], a[i+1] = a[i+1], a[i]
    if a == sorted_a:
        print('Yes')
        exit()
    else:
        a[i], a[i+1] = a[i+1], a[i]

print('No')