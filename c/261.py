N = int(input())

map_data = {}
for i in range(N):
    s = input()
    if s not in map_data:
        map_data.setdefault(s, 0)
        print(s)
    else:
        map_data[s] += 1
        if map_data[s] > 0:
            print(f"{s}({map_data[s]})")