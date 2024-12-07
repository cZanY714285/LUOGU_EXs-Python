n,m  = map(int,input().split())

# store elements in a matrix called 'arr'
arr = []
row_max = []
for _ in range(n):
    a = list(map(int, input().split()))
    arr.append(a)

# build new arr
new_arr = [[0] * n for i in range(m)]
for i in range(n):
    for j in range(m):
        new_arr[j][n - 1 - i] = arr[i][j]

# output the new_arr
for i in range(m):
    for j in range(n):
        print(new_arr[i][j], end=" ")
    print()

