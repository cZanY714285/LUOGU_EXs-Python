n = int(input())
e = 1

for i in range(1,n+1):
    sum = 1
    for j in range(2,i + 1):
        sum *= j
    e += float(1 / sum)

print("%.10f" %e)