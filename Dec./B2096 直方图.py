n = int(input())
arr = list(map(int, input().split()))

# find the max index and number
f_max = max(arr)
index_max = arr.index(f_max)

# count
for i in range(f_max + 1):
    print(arr.count(i))