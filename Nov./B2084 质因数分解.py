n = int(input())
if n % 2 == 0:
    print(int(n / 2))
else:
    mx = int (n / 3)
    for i in range(3,mx):
        if n % i == 0:
            print(int(n / i))
            break
