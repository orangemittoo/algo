N,X = map(int, input().split())
A = list(map(int, input().split()))

left,right = 0, N - 1
while left <= right:
    current = (left + right) // 2
    if A[current] == X:
        print('Yes')
        exit()
    if A[current] < X:
        left = current + 1
    else:
        right = current + 1
    

print('No')
