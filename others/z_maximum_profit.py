import sys

def maximum_profit(n, R):
    result = None
    for idx, r1 in enumerate(R):
        r2 = R[idx + 1:]
        max_val = max(r2) if len(r2) != 0 else None
        if max_val != None:
            r3 = max_val - r1
            result = r3 if result == None or r3 > result else result
    return result

if __name__ == '__main__':
    n = int(sys.argv[1])
    R = [int(sys.argv[i]) for i in range(2, n+2)]
    print(maximum_profit(n, R))