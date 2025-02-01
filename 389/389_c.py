from collections import deque
# クエリの数 最大: 300,000
Q = int(input())
# クエリ
query_list = [list(map(int, input().split())) for _ in range(Q)]

# print(Q)
# print(query_list)

result = deque()
prefix_sum = [0]
remove_total = 0
remove_count = 0

for i in range(Q):
    query = query_list[i]
    if query[0] == 1:
        # 最大: 1,000,000,000
        l = query[1]
        result.append(l)
        # 累積和を追加
        prefix_sum.append(prefix_sum[-1] + l)
    elif query[0] == 2:
        # 最終的に補正する値
        remove_total += result.popleft()
        # オフセットする値
        remove_count += 1
    elif query[0] == 3:
        # 削除分のオフセットを追加した位置の値から、削除分の値を引く
        print(prefix_sum[query[1] - 1 + remove_count] - remove_total)