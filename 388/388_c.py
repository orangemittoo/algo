import bisect

N = int(input())
A = list(map(int, input().split()))

count = 0
for i in range(N):
    a = A[i]
    b = a * 2
    idx = bisect.bisect_left(A, b)
    count += N - idx

print(count)