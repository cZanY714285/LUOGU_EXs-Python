x1,y1 = input().split()
x2,y2 = input().split()
x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)
l = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print('%.3f' %l)