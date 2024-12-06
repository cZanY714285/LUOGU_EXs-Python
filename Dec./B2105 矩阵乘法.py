n,m,k = map(int,input().split())
# input the arr_a
arr_a = []
for _ in range(n):
    a = list(map(int,input().split()))
    arr_a.append(a)

# input the arr_b
arr_b = []
for _ in range(m):
    b = list(map(int,input().split()))
    arr_b.append(b)

# initialize arr_c
arr_c = [[0] * k for _ in range(n)]

# calculate the result
for i in range(n):
    for j in range(k):
        for l in range(m):
            arr_c[i][j] += arr_a[i][l] * arr_b[l][j]

# output arr_c
for i in range(n):
    for j in range(k - 1):
        print(arr_c[i][j],end = ' ')
    print(arr_c[i][k - 1])