def get_point(cx, cy):
    return [
        [cx + 1, cy],
        [cx - 1, cy],
        [cx, cy + 1],
        [cx, cy - 1]
    ]


def get_available_points(range_num, cx, cy, available_points):
    point_list = get_point(cx, cy)
    if range_num not in available_points:
        available_points[range_num] = []
    
    for item in point_list:
        available_points[range_num].append(item)

    if(range_num != 1):
        for point in point_list:
            get_available_points(range_num - 1, point[0], point[1], available_points)
        
    return available_points

N = int(input())
# time_schedule = [int(input()) for _ in range(N)]
time_schedules = [list(map(int, input().split())) for _ in range(N)]

current = [0, 0, 0]
result = []
for schedule in time_schedules:
    time, x, y = schedule
    print('current', current)
    current_time, current_x, current_y = current

    move_count = time - current_time
    available_points = {}
    get_available_points(move_count, current_x, current_y, available_points)
    current = schedule
    for item in available_points[1]:
        item_x, item_y = item
        if item_x == x and item_y == y:
            result.append(True)
            break

print(result)