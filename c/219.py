X = input()
N = int(input())
S = [input() for _ in range(N)]

index_map = {char: idx for idx, char in enumerate(X)}

def custom_key(s):
    return [index_map[char] for char in s]

sorted_s = sorted(S, key=custom_key)

for i in sorted_s:
    print(i)