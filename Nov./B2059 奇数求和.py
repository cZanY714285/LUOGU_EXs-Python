m,n = input().split()
n = int(n)
m = int(m)
if m % 2 == 0:
    m += 1
if n % 2 == 0:
    n -= 1
s = (m + n) * ((n - m) / 2 + 1) / 2
print(int(s))