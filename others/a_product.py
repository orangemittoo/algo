a, b = map(int, input().split())

result = 'Even' if a * b % 2 == 0 else 'Odd'

# print("{} {}".format(a+b+c, s))
print(result)