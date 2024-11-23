s = int(input())
walk = s / 1.2
bike = 27 + 23 + s / 3
if walk > bike:
    print("Bike")
elif walk < bike:
    print("Walk")
else:
    print("All")