H,W = map(int, input().split())
G_list = [list(input()) for _ in range(H)]

i = 1
j = 1
past = {(1,1)}

while True:
    g = G_list[i-1][j-1]

    if g == 'U' and i != 1:
        i -= 1
    elif g == 'D' and i != H:
        i += 1
    elif g == 'L' and j != 1:
        j -= 1
    elif g == 'R' and j != W:
        j += 1
    else:
        break

    if (i, j) in past:
        print(-1)
        exit()

    past.add((i, j))

print(i, j)