def find_second_smallest(numbers):
    smallest = min(numbers)
    numbers.remove(smallest)
    return min(numbers)

# Example usage
numbers = [10, 20, 4, 45, 99]
second_smallest = find_second_smallest(numbers)
print("The second smallest number is:", second_smallest)


