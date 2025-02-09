H, W, N = map(int, input().split())

a_list = []
b_list = []

for _ in range(N):
    a, b = map(int, input().split())
    a_list.append(a)
    b_list.append(b)

unique_rows = sorted(set(a_list))
unique_cols = sorted(set(b_list))

row_map = {v: i + 1 for i, v in enumerate(unique_rows)}
col_map = {v: i + 1 for i, v in enumerate(unique_cols)}

for i in range(N):
    print(row_map[a_list[i]], col_map[b_list[i]])