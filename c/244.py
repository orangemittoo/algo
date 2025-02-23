N = int(input())

used = set()
numbers = set(range(1, N*2+2))
for _ in range(N*2+1):
    kouho = numbers - used
    n = min(kouho)
    used.add(n)
    print(n, flush=True)

    you_n = int(input())
    if you_n == 0:
        exit()
    used.add(you_n)
