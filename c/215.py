import itertools
S,K = list(input().split())

permutations = list(itertools.permutations(S))
a = [''.join(p) for p in permutations]
a = list(set(a))
a.sort()
print(a[int(K)-1])