arr  = [1, 7, 8, 4, 5, 16, 8]
print(arr) 
n = len(arr)
countEven = 0
countodd = 0
for i in range(0, n):
    if arr[i]%2==0 :
        countEven += 1
    else:
        countodd += 1

print("Even Elements count : ",countEven )


print("Odd Elements count : ",countodd)
