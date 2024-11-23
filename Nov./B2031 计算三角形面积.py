x1,y1,x2,y2,x3,y3 = input().split()
x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)
x3 = int(x3)
y3 = int(y3)
s = ((x2 - x1) * (y3 - y2) - (x3 -x2) * (y2 - y1) ) / 2
print('%.2f' %s)