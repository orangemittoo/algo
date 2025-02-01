N = int(input())
time_schedules = [list(map(int, input().split())) for _ in range(N)]
current = [0, 0, 0]
for schedule in time_schedules:
    target_time, target_x, target_y = schedule
    current_time, current_x, current_y = current
    
    move_x = abs(target_x - current_x)
    move_y = abs(target_y - current_y)
    
    move_count = target_time - current_time
    move_diff = move_x + move_y

    is_reachable = move_count >= move_diff and (move_count - move_diff) % 2 == 0

    if is_reachable:
        current = schedule
    else:
        print('No')
        exit()

print('Yes')