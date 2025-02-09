import bisect
N, Q = map(int, input().split())
A = sorted(list(map(int, input().split())))
X_list = [int(input()) for _ in range(Q)]

for i in range(Q):
    point = bisect.bisect_left(A,X_list[i])
    print(N - point)