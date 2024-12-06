m,n = map(int,input().split())

# store in the list 'arr_a'
arr_a = []
for _ in range(m):
    a = map(int,input().split())
    arr_a.extend(a)

# store in the list 'arr_b'
arr_b = []
for _ in range(m):
    b = map(int,input().split())
    arr_b.extend(b)

sum = 0
for i in range(n * m):
    if arr_a[i] == arr_b[i]:
        sum += 1
print('%.2f' % (100 * sum / n / m))