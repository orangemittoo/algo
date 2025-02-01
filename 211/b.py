w_list = ['H','2B','3B','HR']
input_list = []
for _ in range(4):
    input_list.append(input())

for s in w_list:
    if s not in input_list:
        print('No')
        exit()

print('Yes')