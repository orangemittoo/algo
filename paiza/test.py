N,X = list(map(int, input().split()))
Q = [list(input().split()) for _ in range(N)]

elevator = []
weight_total = 0
for i in range(N):
    query = Q[i]
    if query[0] == 'ride':
        for person_w in query[2:]:
            person_w = int(person_w)
            if weight_total + person_w <= X:
                elevator.append(person_w)
                weight_total += person_w
    else:
        for _ in range(int(query[1])):
            person_w = elevator.pop()
            weight_total -= person_w

print(len(elevator))
print(weight_total)