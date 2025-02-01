n = input()
a = list(map(int, input().split()))

def check_even(arr, result):
    # print(arr)
    next_arr = []
    even_count = 0
    for v in arr:
        even_count += 1 if v % 2 == 0 else 0
        next_arr.append(int(v / 2))

    if len(arr) == even_count:
        result += 1
        return check_even(next_arr, result)
    
    return result

print(check_even(a, 0))