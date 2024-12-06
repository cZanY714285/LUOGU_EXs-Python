n = int(input())

# input the number in the array
arr = []
for i in range(n):
    arr.append(float(input()))

# find the max & min
arr_max = max(arr)
arr_min = min(arr)
arr_sum = sum(arr)

# find the average
average =(arr_sum - arr_max - arr_min) / (n - 2)

# remove the max & min
arr.remove(max(arr))
arr.remove(min(arr))

#find the max gap
positive_gap = max(arr) - average
negative_gap = average - min(arr)
gap = max(positive_gap, negative_gap)

# output the result
print('%.2f %.2f' % (average,gap))