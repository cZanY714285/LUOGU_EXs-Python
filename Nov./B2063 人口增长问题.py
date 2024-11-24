x,n = input().split()
x = float(x)
n = int(n)
x *= 1.001 ** n
print('%.4f' % x)