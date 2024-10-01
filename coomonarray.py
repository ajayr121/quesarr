a = [1, 2, 3, 4, 5]
b = [5, 2, 6, 3, 9]

result = (set(a) & set(b))

if result:
   print("The common elements are:", result)
else:
   print("No common elements present in two arrays")