n = int(input())

# start the loop
for i in range(1,n + 1):
    if i == 1:
        light = False

    # turn on = True; turn off = False
    elif i % 2 == 1:
        light = False
    else:
        light = True

    # keep turning on and off again and again
    for j in range(3,i + 1):
        if i % j == 0:
            light = not light

    # print the number
    if light == False:
        print(i,end = ' ')