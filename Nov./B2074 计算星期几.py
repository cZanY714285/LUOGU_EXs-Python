a,b = input().split()
a = int(a)
b = int(b)
n = a ** b % 7

if n == 0:
    print("Sunday")
elif n == 1:
    print("Monday")
elif n == 2:
    print("Tuesday")
elif n == 3:
    print("Wednesday")
elif n == 4:
    print("Thursday")
elif n == 5:
    print("Friday")
elif n == 6:
    print("Saturday")