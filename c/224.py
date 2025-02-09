import itertools
N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

count = 0
for (x1, y1),(x2, y2), (x3, y3) in itertools.combinations(XY, 3):
    if (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1) != 0:
        count += 1
print(count)
