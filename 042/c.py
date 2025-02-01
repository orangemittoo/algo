N,K = list(map(int, input().split()))
D = list(map(str, input().split()))
D = set(D)

while True:
    if not any(d in str(N) for d in D):
        print(N)
        exit()
    N += 1
