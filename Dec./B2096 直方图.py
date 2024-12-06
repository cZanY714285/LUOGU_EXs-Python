n = int(input())
arr = list(map(int, input().split()))

# find the max number
f_max = max(arr)

# count every element that appears in the arr
count = [0] * (f_max + 1)
for i in arr:
    count[i] += 1

# output the count range from 0 to (f_max + 1)
for i in range(f_max + 1):
    print(count[i])