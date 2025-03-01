N = int(input())
A = list(map(int, input().split()))

even_list = []
odd_list = []
for a in A:
    if a%2 == 0:
        even_list.append(a)
    else:
        odd_list.append(a)

even_list.sort()
odd_list.sort()

even_max = even_list[-1] + even_list[-2] if len(even_list) > 1 else -1
odd_max = odd_list[-1] + odd_list[-2] if len(odd_list) > 1 else -1

print(max(even_max, odd_max))