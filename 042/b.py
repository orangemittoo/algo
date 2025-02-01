N,L = list(map(int,input().split()))

str_list = []
for i in range(N):
    str_list.append(input())

str_list.sort()
print("".join(str_list))