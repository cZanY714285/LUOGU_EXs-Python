n,m = map(int,input().split())
# input the arr
arr = []
for _ in range(n):
    a = map(int,input().split())
    arr.extend(a)

# store elements in re_arr
re_arr = [0] * (n * m)
for i in range(n):
    for j in range(m):
        re_arr[j * n + i] = arr[i * m + j]

# output re_arr
for j in range(m):
    for i in range(n - 1):
        print(re_arr[j * n + i], end=" ")
    print(re_arr[j * n + n - 1])

