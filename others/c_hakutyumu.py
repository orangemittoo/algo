S = input()

word_list = ['dream', 'dreamer', 'erase', 'eraser']

while S:
    matched = False
    for word in word_list:
        if S.endswith(word):
            S = S[:len(S) - len(word)]
            matched = True
            break
    if not matched:
        print('NO')
        exit()

print('YES')