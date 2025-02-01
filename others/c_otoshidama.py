N, Y = list(map(int, input().split()))

for ichiman in range(N+1):
    gosen_range = range(N+1 - ichiman)
    for gosen in gosen_range:
        sen = N - ichiman - gosen
        total = ichiman * 10000 + gosen * 5000 + sen * 1000
        if total == Y:
            print(ichiman, gosen, sen)
            exit()

print(-1, -1, -1)