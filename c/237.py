S = list(input())

left = 0
right = len(S) - 1

while left < right:
    if S[left] == S[right]:
        left += 1
        right -= 1
    elif 'a' == S[right]:
        right -= 1
    else:
        print('No')
        exit()
print('Yes')