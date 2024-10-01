# code first 
arr = [12,34,55,45,76,87,10,90,121]
mini = arr[0]
maxi = arr[0]

for i in range(len(arr)):
    if arr[i]<mini:
        mini = arr[i]

    if arr[i]>maxi:
        maxi = arr[i]

print(mini)
print(maxi)

'''# code second
arr = [12,34,55,45,76,87,10,90,121]
print(min(arr))
print(max(arr))

# code third 
arr = [12,34,55,45,76,87,10,90,121]
arr.sort()

print(arr[0])
print(arr[-1])'''