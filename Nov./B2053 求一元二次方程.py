a,b,c = input().split()
a = float(a)
b = float(b)
c = float(c)
if b * b - 4 * a * c < 0:
    print("No answer!")
elif b * b - 4 * a * c == 0:
    x = - b / 2 / a
    print('x1=x2=%.5f' %x)
else:
    x1 = (- b -(b * b - 4 * a * c) ** 0.5 )/ 2 / a
    x2 = (- b +(b * b - 4 * a * c) ** 0.5 )/ 2 / a
    print('x1=%.5f;x2=%.5f' %(min(x1,x2),max(x1,x2)))