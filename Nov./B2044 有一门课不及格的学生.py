a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a < 60 <= b and c >= 60:
    print("1")
elif a >= 60 > b and c >= 60:
    print("1")
elif a >= 60 > c and b >= 60:
    print("1")
else:
    print("0")