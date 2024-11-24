n = int(input())
while n != 1:
    if n % 2 == 0:
        print(n,end = "")
        n = int(n / 2)
        print(f'/2=%d' %n)
    else:
        print(n,end = "")
        n = 3 * n + 1
        print(f"*3+1=%d" %n)
print("End")
