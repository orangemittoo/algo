# https://atcoder.jp/contests/abc386

K = int(input())
S = input()
T = input()

if S == T:
    print('Yes')
    exit()

lenS, lenT = len(S), len(T)

if abs(lenS - lenT) > 1:
    print('No')
    exit()

if lenS == lenT:
    count = sum(1 for i in range(lenS) if S[i] != T[i])
    print('Yes' if count == 1 else 'No')
    exit()

if lenS > lenT:
    long, short = S, T
else:
    long, short = T, S

i = 0
while i < len(short) and short[i] == long[i]:
    i += 1

j = 0
while j < len(short) and short[-(j+1)] == long[-(j+1)]:
    j += 1

if i + j >= len(short):
    print('Yes')
else:
    print('No')