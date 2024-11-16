import numpy as np

# Creating a 1D NumPy array
arr1 = np.array([1, 2, 3, 4, 5])

# Display the array
print("1D NumPy Array:")
print(arr1)
print()

# Accessing and manipulating array elements
print("Accessing and Manipulating Array Elements:")
print("First element:", arr1[0])
print("Last element:", arr1[-1])
print("Slice from index 1 to 3:", arr1[1:4])
print("Array elements multiplied by 2:", arr1 * 2)
print()

# Creating a 2D NumPy array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# Display the array
print("2D NumPy Array:")
print(arr2)
print()

# Array operations and functions
print("Array Operations and Functions:")
print("Sum of all elements:", np.sum(arr2))
print("Mean of all elements:", np.mean(arr2))
print("Maximum element:", np.max(arr2))
print("Reshaped array (2x3 to 3x2):")
print(np.reshape(arr2, (3, 2)))
print()

# Generating random numbers
random_nums = np.random.randint(low=0, high=10, size=(3, 4))

# Display the random numbers
print("Randomly Generated Numbers:")
print(random_nums)
print()
