h,r = input().split()
h = int(h)
r = int(r)
v = 3.14 * h * r ** 2
n = int(20000 / v) + 1
print(n)