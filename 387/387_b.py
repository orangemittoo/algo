# https://atcoder.jp/contests/abc387

X = int(input())

list_v = list(range(1, 10))

result = 0
for i in list_v:
    for j in list_v:
        r = i*j
        if r != X:
            result += r

print(result)