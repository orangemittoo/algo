N, A, B = map(int, input().split())

# N以下の整数
nums = list(range(N+1))

result = 0
for v in nums:
    # X = 0
    # for n in str(v):
    #     X += int(n)
    X = sum(map(int, str(v)))
    
    # 各桁の和がA <= X <= B であるかどうか
    if A <= X <= B:
        result += int(v)
    
print(result)