A,B,C = list(map(int,input().split()))

five = 0
seven = 0
for i in [A, B, C]:
    if i == 5:
        five += 1
    if i == 7:
        seven += 1

print('YES' if five == 2 and seven == 1 else 'NO')