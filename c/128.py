N,M = list(map(int, input().split()))
ss = []
for _ in range(M):
    ss.append(list(map(int, input().split())))
pp = list(map(int, input().split()))

count = 0
for bit in range(1 << N):
    valid = True
    for i in range(M):
        record = ss[i]
        k = record[0]
        r = record[1:]
        on_count = 0
        for switch in r:
            if (bit >> (switch - 1)) & 1:
                on_count += 1
        if on_count % 2 != pp[i]:
            valid = False
            break
    if valid:
        count += 1

print(count)