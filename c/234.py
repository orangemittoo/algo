K = int(input())

binary_repr = bin(K)[2:]
result = binary_repr.replace('1', '2')

print(result)