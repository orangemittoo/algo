N = input()
a_list =  list(map(int, input().split()))

# リストを降順に並べる
a_list.sort(reverse=True)


# Alice/Bobの点数
alice = 0
bob = 0
for idx, a in enumerate(a_list, start = 1):
    if idx % 2 == 0:
        bob += a
    else:
        alice += a

# result: Aliceの点数 - Bobの変数
print(alice - bob)