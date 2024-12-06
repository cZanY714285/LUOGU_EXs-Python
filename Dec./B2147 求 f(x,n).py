x,n = map(float,input().split())
n = int(n)
f = (1 + x) ** 0.5
for i in range(2,n + 1):
    f = (i + f) ** 0.5
print('%.2f' % f)