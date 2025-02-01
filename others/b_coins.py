# 入力
A = int(input())  # 500円玉の枚数
B = int(input())  # 100円玉の枚数
C = int(input())  # 50円玉の枚数
X = int(input())  # 合計金額

# 組み合わせをカウント
count = 0

# 全探索
for i in range(A + 1):       # 500円玉を0〜A枚選ぶ
    for j in range(B + 1):   # 100円玉を0〜B枚選ぶ
        for k in range(C + 1): # 50円玉を0〜C枚選ぶ
            # 合計金額がXに一致するか確認
            if 500 * i + 100 * j + 50 * k == X:
                count += 1

# 出力
print(count)