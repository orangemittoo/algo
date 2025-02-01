# a, b = map(int, input().split())
a = input()

# arr = [int(val) for val in a]

result = 0

for val in list(a):
    if int(val) == 1:
        result += 1


print(result)