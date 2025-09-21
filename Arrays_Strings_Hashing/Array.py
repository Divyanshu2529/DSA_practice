# Array

# An array is a collection of items of the same variable type that are stored at contiguous (Same) memory locations.


#Types of Arrays: Arrays can be classified in two ways:

# On the basis of Size - Fixed Size, Dynamic Size
# On the basis of Dimensions - One Dimentional, Multidimentional ( Two and three Dimentional)


# Fixed Size: We cannot alter or update the size of this array and Fixed size of memory will be allocated for storage.

# Dynamic Size (Python only have these): The size of the array changes as per user requirements during execution of code. The memory is mostly dynamically allocated and de-allocated in these arrays.


# One Dimentional Array: A row where elements are stored one after another.  

# Two-Dimensional Array(2-D Array or Matrix): 2-D Multidimensional arrays can be considered as an array of arrays or as a matrix consisting of rows and columns.

# Three-Dimensional Array(3-D Array): A 3-D Multidimensional array contains three dimensions, so it can be considered an array of two-dimensional arrays.



# Operations in Array

# -) Traversal in Array: Traversal in an array refers to the process of accessing each element in the array sequentially, typically to perform a specific operation, such as searching, sorting, or modifying the elements.

# There are two type of Traversal- Linear and Reverse Treversal 

# LINEAR TREVERSAL 
# Linear traversal is the process of visiting each element of an array sequentially, starting from the first element and moving to the last element. During this traversal, each element is processed (printed, modified, or checked) one after the other, in the order they are stored in the array. This is the most common and straightforward way of accessing the elements of an array.

# Code 

# arr = [1,2,3,4,5]
# print("Linear Traversal:", end=" ") # we use end= " " so that it priend next to each other

# for i in arr :
#     print(i, end=" ")

# print()

# Output: Linear Traversal: 1 2 3 4 5 

# Time Complexity: O(n)
# Auxiliary Space: O(1)


# REVERSE TREVERSAL
# Reverse traversal is the process of visiting each element of an array starting from the last element and moving towards the first element. This method is useful when you need to process the elements of an array in reverse order. In this type of traversal, you begin from the last index (the rightmost element) and work your way to the first index (the leftmost element).

# Code

# arr = [1, 2, 3, 4, 5]

# print("Reverse Traversal: ", end="")

# for i in range(len(arr) - 1, -1, -1):
#     print(arr[i], end=" ")
    
# print()

# Output: Reverse Traversal: 5 4 3 2 1 

# Time Complexity: O(n)
# Auxiliary Space: O(1)


# Methods of Array Traversal

# 1) Using For Loop

# Code

# arr = [10, 20, 30, 40, 50]

# print("Traversal using for loop: ", end=' ')
# for i in arr:
#     print(i, end=' ')
# print()

# Output: Traversal using for loop: 10 20 30 40 50 

# Time Complexity: O(n)
# Auxiliary Space: O(1)



# 2) Using While Loop

# Code

# arr = [10, 20, 30, 40, 50]

# n = len(arr)
# i = 0

# print("Traversal using while loop: ", end=" ")
# while i < n:
#     print(arr[i], end=" ")
#     i += 1
# print()

# Output: Traversal using while loop: 10 20 30 40 50 

# Time Complexity: O(n)
# Auxiliary Space: O(1)



# 3) Using Foreach Loop (Range-based For Loop)

# Code

# arr = [10, 20, 30, 40, 50]

# print("Traversal using foreach loop:", end=' ')
# for value in arr:
#     print(value, end=' ')
# print()

# Output: Traversal using foreach (range-based for) loop: 10 20 30 40 50 

# Time Complexity: O(n)
# Auxiliary Space: O(1)


# Applications of Array Traversal 

# 1. Searching Elements 
# Traversal is often used to search for an element in an array. By visiting each element of the array sequentially, we can compare each element with the target value to determine if it exists.

# Code

# arr = [10, 20, 30, 40, 50]
# target = 30
# found = False

# # Linear search using traversal
# for i in range(len(arr)):
#     if arr[i] == target:
#         found = True
#         break

# if found:
#     print("Element found!")
# else:
#     print("Element not found!")
    
    
# Output: Element found!

# Time Complexity: O(n)
# Auxiliary Space: O(1)



# 2. Modifying Elements
# Array traversal is also used to modify the elements of the array. This could involve updating values, changing the order, or applying some mathematical operations to each element. For example, you can multiply every element of an array by a constant, or increase each value by 1.

# Code 

# arr = [10, 20, 30, 40, 50]

# # Modifying elements using traversal (increasing each by 5)
# for i in range(len(arr)):
#     arr[i] += 5

# # Print modified array
# print("Modified array:", end=' ')
# for num in arr:
#     print(num, end=' ')
# print()

# Output: Modified array: 15 25 35 45 55 

# Time Complexity: O(n)
# Auxiliary Space: O(1)