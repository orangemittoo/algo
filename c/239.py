def knight_moves(x, y):
    return {(x+2, y+1), (x+2, y-1), (x-2, y+1), (x-2, y-1),
            (x+1, y+2), (x+1, y-2), (x-1, y+2), (x-1, y-2)}

x1, y1, x2, y2 = map(int, input().split())

moves1 = knight_moves(x1, y1)
moves2 = knight_moves(x2, y2)

if moves1 & moves2:
    print("Yes")
else:
    print("No")