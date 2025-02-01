# https://atcoder.jp/contests/abc386

A,B,C,D = list(map(int, input().split()))

l = [A,B,C,D]
ul = list(set(l))

if len(ul) != 2:
    print('No')
    exit()

print('Yes')
