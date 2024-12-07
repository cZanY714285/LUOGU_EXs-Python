n,m  = map(int,input().split())

# store elements in a matrix called 'arr'
arr = []
for _ in range(n):
    a = list(map(int, input().split()))
    arr.append(a)

# define a function: 四舍五入
def float_to_int(a_float):
    if a_float % 1 >= 0.5:
        return int(a_float) + 1
    else:
        return int(a_float)

# build new arr
new_arr = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if i == 0 or i == (n - 1) or j == 0 or j == (m - 1):
            new_arr[i][j] = arr[i][j]
        else:
            x = (arr[i][j] +
                     arr[i + 1][j] +
                     arr[i - 1][j] +
                     arr[i][j + 1] +
                     arr[i][j - 1]) / 5
            new_arr[i][j] = float_to_int(x)

# output the new_arr
for i in range(n):
    for j in range(m):
        print(new_arr[i][j], end=" ")
    print()
