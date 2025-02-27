import itertools
N,M = map(int, input().split())

target = [i for i in range(1, M+1)]
for item in list(itertools.combinations(target, N)):
    print(*item)