N,M = map(int, input().split())
S_list = input().split()
T_list = set(input().split())

for i in range(N):
    if S_list[i] in T_list:
        print('Yes')
    else:
        print('No')