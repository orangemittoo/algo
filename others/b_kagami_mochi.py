

N = int(input())
d_list = [int(input()) for _ in range(N)]

d_list = list(set(d_list))
d_list.sort()

print(len(d_list))