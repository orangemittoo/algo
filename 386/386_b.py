# https://atcoder.jp/contests/abc386

S = str(input())

ans = []
int_s = list(S)

while len(int_s) != 0:
    s = int(int_s.pop(0))
    if s == 0 and len(int_s) > 0:
        ss = int(int_s.pop(0))
        if ss == 0:
            ans.append('00')
        else:
            ans.append(s)
            ans.append(ss)
    else:
        ans.append(s)

print(len(ans))


# 100000007
# 1,00,00,00,0,7