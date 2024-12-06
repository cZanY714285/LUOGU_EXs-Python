n = int(input())

# input the age of every patient
arr = list(map(int, input().split()))

# initialize the sum of every scale
sum_1,sum_2,sum_3,sum_4 = 0,0,0,0

# count
for i in range(n):
    if arr[i] <= 18:
        sum_1 += 1
    elif arr[i] <= 35:
        sum_2 += 1
    elif arr[i] <= 60:
        sum_3 += 1
    else:
        sum_4 += 1
print('%.2f%%' %(100 * sum_1 / n))
print('%.2f%%' %(100 * sum_2 / n))
print('%.2f%%' %(100 * sum_3 / n))
print('%.2f%%' %(100 * sum_4 / n))
