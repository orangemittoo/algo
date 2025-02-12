N = int(input())

fibo = [1, 1]
# for i in range(2, N+1):
#     fibo.append(fibo[i-2] + fibo[i-1])
# print(fibo)
i = 2
while True:
    value = fibo[i-2] + fibo[i-1]
    if value > N:
        break
    fibo.append(value)
    i += 1

print(fibo)