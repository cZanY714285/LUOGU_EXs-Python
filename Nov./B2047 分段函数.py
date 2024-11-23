x = float(input())
if 0 <= x < 5:
    y = 2.5 - x
    print('%.3f' %y)
elif 5 <= x < 10:
    y = 2 - 1.5 * (x - 3)** 2
    print('%.3f' %y)
else :
    y = x / 2 - 1.5
    print('%.3f' %y)
