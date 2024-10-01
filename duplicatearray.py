my_list = [1, 2, 5, 6, 8, 9, 3, 4, 8, 9, 1, 8]
print("The list is :")
print(my_list)
print("The duplicate elements in the list are : ")
for i in range(0, len(my_list)):
   for j in range(i+1, len(my_list)):
      if(my_list[i] == my_list[j]):
         print(my_list[j])