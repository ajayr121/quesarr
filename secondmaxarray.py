'''arr = [10,20,34,55,67,34,87,98]
arr.sort()

print(arr[-2])'''

def find_second_largest(numbers):
    largest = max(numbers)
    numbers.remove(largest)
    return max(numbers)

# Example usage
numbers = [10, 20, 4, 45, 99]
second_largest = find_second_largest(numbers)
print("The second largest number is:", second_largest)
