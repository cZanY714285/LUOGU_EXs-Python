# input the arr
arr = []
for _ in range(5):
    a = list(map(int,input().split()))
    arr.append(a)

# switch
m,n = map(int,input().split())
m -= 1
n -= 1
for i in range(5):
    arr[m][i], arr[n][i] = arr[n][i], arr[m][i]

# output the new arr
for i in range(5):
    for j in range(4):
        print(arr[i][j],end = ' ')
    print(arr[i][4])