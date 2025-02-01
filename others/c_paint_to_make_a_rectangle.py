H, W = list(map(int, input().split()))
S = [list(input()) for _ in range(H)]

row_min = None
row_max = None
col_min = None
col_max = None

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            # 最初の黒マスが見つかったとき
            if row_min is None:
                row_min = i
                row_max = i
                col_min = j
                col_max = j
            else:
                # 2回目以降は min/max を随時更新
                if i < row_min:
                    row_min = i
                if i > row_max:
                    row_max = i
                if j < col_min:
                    col_min = j
                if j > col_max:
                    col_max = j

for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            # 範囲内にあったらNG
            if row_min <= i <= row_max and col_min <= j <= col_max:
                print('No')
                exit()
        if S[i][j] == '#':
            # 範囲外にあったらNG
            if not (row_min <= i <= row_max and col_min <= j <= col_max):
                print('No')
                exit()


print('Yes')


