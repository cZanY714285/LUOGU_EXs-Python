n,m = map(int,input().split())

# input elements in arr_a
arr_a = []
for _ in range(n):
    a = list(map(int,input().split()))
    arr_a.extend(a)

# input elements in arr_b
arr_b = []
for _ in range(n):
    b = list(map(int, input().split()))
    arr_b.extend(b)

#input elements in the same position
for i in range(n):
    for j in range(m - 1):
        print(arr_a[i * m + j]+arr_b[i * m + j],end = ' ')
    print(arr_a[i * m + m - 1]+arr_b[i * m + m - 1])
