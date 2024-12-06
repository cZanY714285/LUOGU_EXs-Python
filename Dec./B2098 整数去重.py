n = int(input())
arr = list(map(int, input().split()))

# set up a new arr
new_arr = []
for i in range(n):
    # if there's no such element in new_arr, then add it to new_arr
    if new_arr.count(arr[i]) == 0:
        new_arr.append(arr[i])
        print(arr[i],end = ' ')