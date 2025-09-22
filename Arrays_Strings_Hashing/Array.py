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

arr = [1,2,3,4,5]
print("Linear Traversal:", end=" ") # we use end= " " so that it priend next to each other

for i in arr :
    print(i, end=" ")

print()

# Output: Linear Traversal: 1 2 3 4 5 

# Time Complexity: O(n)
# Auxiliary Space: O(1)


# REVERSE TREVERSAL
# Reverse traversal is the process of visiting each element of an array starting from the last element and moving towards the first element. This method is useful when you need to process the elements of an array in reverse order. In this type of traversal, you begin from the last index (the rightmost element) and work your way to the first index (the leftmost element).

# Code

arr = [1, 2, 3, 4, 5]

print("Reverse Traversal: ", end="")

for i in range(len(arr) - 1, -1, -1):
    print(arr[i], end=" ")
    
print()

# Output: Reverse Traversal: 5 4 3 2 1 

# Time Complexity: O(n)
# Auxiliary Space: O(1)


# Methods of Array Traversal

# 1) Using For Loop

# Code

arr = [10, 20, 30, 40, 50]

print("Traversal using for loop: ", end=' ')
for i in arr:
    print(i, end=' ')
print()

# Output: Traversal using for loop: 10 20 30 40 50 

# Time Complexity: O(n)
# Auxiliary Space: O(1)



# 2) Using While Loop

# Code

arr = [10, 20, 30, 40, 50]

n = len(arr)
i = 0

print("Traversal using while loop: ", end=" ")
while i < n:
    print(arr[i], end=" ")
    i += 1
print()

# Output: Traversal using while loop: 10 20 30 40 50 

# Time Complexity: O(n)
# Auxiliary Space: O(1)



# 3) Using Foreach Loop (Range-based For Loop)

# Code

arr = [10, 20, 30, 40, 50]

print("Traversal using foreach loop:", end=' ')
for value in arr:
    print(value, end=' ')
print()

# Output: Traversal using foreach (range-based for) loop: 10 20 30 40 50 

# Time Complexity: O(n)
# Auxiliary Space: O(1)


# Applications of Array Traversal 

# 1. Searching Elements 
# Traversal is often used to search for an element in an array. By visiting each element of the array sequentially, we can compare each element with the target value to determine if it exists.

# Code

arr = [10, 20, 30, 40, 50]
target = 30
found = False

# Linear search using traversal
for i in range(len(arr)):
    if arr[i] == target:
        found = True
        break

if found:
    print("Element found!")
else:
    print("Element not found!")
    
    
# Output: Element found!

# Time Complexity: O(n)
# Auxiliary Space: O(1)



# 2. Modifying Elements
# Array traversal is also used to modify the elements of the array. This could involve updating values, changing the order, or applying some mathematical operations to each element. For example, you can multiply every element of an array by a constant, or increase each value by 1.

# Code 

arr = [10, 20, 30, 40, 50]

# Modifying elements using traversal (increasing each by 5)
for i in range(len(arr)):
    arr[i] += 5

# Print modified array
print("Modified array:", end=' ')
for num in arr:
    print(num, end=' ')
print()

# Output: Modified array: 15 25 35 45 55 

# Time Complexity: O(n)
# Auxiliary Space: O(1)




# Insertions : At Beginning, At given position and At the end.

# At Beginning

# [Approach 1] Using Built-In Methods

# Code 

arr = [10, 20, 30, 40]
element = 50
print("Array before insertion")
for i in range(len(arr)):
	print(arr[i], end=" ")

# Insert element at the beginning
arr.insert(0, element)

print("\nArray after insertion")
for i in range(len(arr)):
    print(arr[i], end=" ")


# Output: Array before insertion
# 10 20 30 40 
# Array after insertion
# 50 10 20 30 40 

# Time Complexity: O(n)


# [Approach 2] Using Custom Method

# Code 


arr = [10, 20, 30, 40, 0]
n = 4
element = 50
    
print("Array before insertion")
for i in range(n):
    print(arr[i], end=" ")
    
# Shift all elements to the right
for i in range(n - 1, -1, -1):
    arr[i + 1] = arr[i]

# Insert new element at the beginning
arr[0] = element

print("\nArray after insertion")
for i in range(n + 1):
    print(arr[i], end=" ") 


# Output: Array before insertion
# 10 20 30 40 
# Array after insertion
# 50 10 20 30 40 

# Time Complexity: O(n)






# Insert Element at a Given Position in an Array

# [Approach 1] Using Built-In Methods

# Code 

if __name__ == "__main__":
    arr = [10, 20, 30, 40]
    ele = 50
    pos = 2
    print("Array before insertion")
    print(arr)

    # Insert element at the given position
    arr.insert(pos - 1, ele)

    print("Array after insertion")
    print(arr)

# Output
# Array before insertion
# 10 20 30 40 
# Array after insertion
# 10 50 20 30 40 

# Time Complexity: O(n)



# [Approach 2] Using Custom Method

# Code 

arr = [10, 20, 30, 40, 0]
n = 4
element = 50
    
print("Array before insertion")
for i in range(n):
    print(arr[i], end=" ")
    
# Shift all elements to the right
for i in range(n - 1, -1, -1):
    arr[i + 1] = arr[i]

# Insert new element at the beginning
arr[0] = element

print("\nArray after insertion")
for i in range(n + 1):
    print(arr[i], end=" ")


# Output
# Array before insertion
# 10 20 30 40 
# Array after insertion
# 10 50 20 30 40 

# Time Complexity: O(n)




# Insert Element at the End of an Array

# [Approach 1] Using Built-In Methods

# Code 

if __name__ == "__main__":
    arr = [10, 20, 30, 40]
    ele = 50
    print("Array before insertion")
    for i in range(len(arr)):
        print(arr[i], end=" ")

    # Insert element at the end
    arr.append(ele)

    print("\nArray after insertion")
    for i in range(len(arr)):
        print(arr[i], end=" ")


# Array before insertion
# 10 20 30 40 
# Array after insertion
# 10 20 30 40 50 

# Time Complexity: O(1)
# Auxiliary Space: O(1)


# [Approach 2] Using Custom Method

# Code 

if __name__ == "__main__":
    n = 4
    arr = [10, 20, 30, 40, 0]
    ele = 50

    print("Array before insertion")
    for i in range(n):
        print(arr[i], end=" ")

    # Inserting element at the end of the array
    arr[n] = ele

    print("\nArray after insertion")
    for i in range(n + 1):
        print(arr[i], end=" ")


# Output
# Array before insertion
# 10 20 30 40 
# Array after insertion
# 10 20 30 40 50 

# Time Complexity: O(1)
# Auxiliary Space: O(1)




# Deletion : From Beginning, Given Position, First Occurrence, All occurrences and From End

# Delete an Element from the Beginning of an Array

# [Approach 1] Using Built-In Methods

# Code 

arr = [10, 20, 30, 40]

print("Array before deletion")
for i in range(len(arr)):
    print(arr[i], end=" ")

# Remove the first element 
del arr[0]

print("\nArray after deletion")
for i in range(len(arr)):
    print(arr[i], end=" ")
    

# Output
# Array before deletion
# 10 20 30 40 
# Array after deletion
# 20 30 40 

# Time Complexity: O(n) 
# Auxiliary Space: O(1)


# [Approach 2] Using Custom Methods

# Code 


if __name__ == "__main__":
    arr = [10, 20, 30, 40]
    n = len(arr)
  
    print("Array before deletion")
    for i in range(n):
        print(arr[i], end=" ")

    # Shift all the elements 1 position to the left
    # starting from second element
    for i in range(1, n):
        arr[i - 1] = arr[i]
	
    # Reduce the array size by 1
    n -= 1

    print("\nArray after deletion")
    for i in range(n):
        print(arr[i], end=" ")

#Output
# Array before deletion
# 10 20 30 40 
# Array after deletion
# 20 30 40 

# Time Complexity: O(n)
# Auxiliary Space: O(1)




#Delete an Element from a Given Position in an Array

# [Approach 1] Using Built-In Methods

# Code

arr = [10, 20, 30, 40]
pos = 2

print("Array before deletion")
for num in arr:
    print(num, end=" ")

# Delete the element at the specified position
del arr[pos - 1]

print("\nArray after deletion")
for num in arr:
    print(num, end=" ")


# Output
# Array before deletion
# 10 20 30 40 
# Array after deletion
# 10 30 40 

# Time Complexity: O(n)
# Auxiliary Space: O(1)



# [Approach 2] Using Custom Method


# Code


if __name__ == "__main__":
    arr = [10, 20, 30, 40]
    n = len(arr)
    pos = 2

    print("Array before deletion")
    for i in range(n):
        print(arr[i], end=" ")

    # Delete the element at the given position
    for i in range(pos, n):
        arr[i - 1] = arr[i]

    if pos <= n:
        n -= 1

    print("\nArray after deletion")
    for i in range(n):
        print(arr[i], end=" ")


# Output
# Array before deletion
# 10 20 30 40 
# Array after deletion
# 10 30 40 

# Time Complexity: O(n)
# Auxiliary Space: O(1)




# Delete First Occurrence of Given Element from an Array

# [Approach 1] Using Built-In Methods

# Code 
if __name__ == "__main__":

	arr = [10, 20, 20, 20, 30]
	ele = 20

	print("Array before deletion")
	for num in arr:
		print(num, end=" ")

    # Remove the element if it is present in array
	if ele in arr:
		arr.remove(ele)

	print("\nArray after deletion")
	for num in arr:
		print(num, end=" ")
  
# Output
# Array before deletion
# 10 20 20 20 30 
# Array after deletion
# 10 20 20 30 

# Time Complexity: O(n)
# Auxiliary Space: O(1)



# [Approach 2] Using Custom Methods

# Code 


if __name__ == "__main__":
    arr = [10, 20, 20, 20, 30]
    n = len(arr)
    ele = 20

    print("Array before deletion")
    for i in range(n):
        print(arr[i], end=" ")
    
    found = False
    for i in range(n):
      
        # If the element has been found previously,
        # shift the current element to the left
        if found:
            arr[i - 1] = arr[i]
        
        # check if the current element is equal to
        # the element to be removed
        elif arr[i] == ele:
            found = True
    
    # If element was found, reduce the size of array
    if found:
        n -= 1
    
    print("\nArray after deletion")
    for i in range(n):
        print(arr[i], end=" ")
        
        
        
# Output
# Array before deletion
# 10 20 20 20 30 
# Array after deletion
# 10 20 20 30 

# Time Complexity: O(n)
# Auxiliary Space: O(1)






# Remove All Occurrences of an Element in an Array
# The idea is to iterate over the array while maintaining a subarray at the beginning that contains only the elements which are not equal to ele. So, we can use a counter, say k to track the ending point of this subarray and whenever we encounter an element which is not equal to ele, we can add the element at kth index and increment the value of k.

# Code

def removeElement(arr, ele):
  
    # Initialize the counter for the 
    # elements not equal to ele    
    k = 0
    for i in range(len(arr)):

        # Place the element which is not 
        # equal to ele at the kth position
        if arr[i] != ele:
            arr[k] = arr[i]  
            
            # Increment the count of 
            # elements not equal to ele
            k += 1             
              
    return k 
  
if __name__ == "__main__":
    arr = [0, 1, 3, 0, 2, 2, 4, 2]
    ele = 2
    print(removeElement(arr, ele))
    
# Output
# 5

# Time Complexity: O(n)
# Auxiliary Space: O(1)




# Delete an Element from the end of an array

# [Approach 1] Using Built-In Methods
#Code

arr = [10, 20, 30, 40]

print("Array before deletion")
for ele in arr:
    print(ele, end=" ")

# Remove the last element from the array
arr.pop()

print("\nArray after deletion")
for ele in arr:
    print(ele, end=" ")

# Output
# Array before deletion
# 10 20 30 40 
# Array after deletion
# 10 20 30 

# Time Complexity: O(1) 
# Auxiliary Space: O(1)



# [Approach 2] Using Custom Method
Code

if __name__ == "__main__":
    arr = [10, 20, 30, 40]
    n = len(arr)
  
    print("Array before deletion")
    for i in range(n):
        print(arr[i], end=" ")
    
    # Reduce the array size by 1
    n -= 1

    print("\nArray after deletion")
    for i in range(n):
        print(arr[i], end=" ")
        
        
# Output
# Array before deletion
# 10 20 30 40 
# Array after deletion
# 10 20 30 

# Time Complexity: O(1) 
# Auxiliary Space: O(1)







# Searching: Linear Search and Binary Search

# Linear Search
# In Linear Search, we iterate over all the elements of the array and check if it the current element is equal to the target element. If we find any element to be equal to the target element, then return the index of the current element. Otherwise, if no element is equal to the target element, then return -1 as the element is not found. Linear search is also known as sequential search.

# Code


def search(arr, x):
    n = len(arr)
    
    # Iterate over the array in order to
    # find the key x
    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1

if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 10

    result = search(arr, x)
    if(result == -1):
        print("Element is not present in array")
    else:
        print("Element is present at index", result)


# Output
# Present at Index 3

# Time Complexity:

# Best Case: In the best case, the key might be present at the first index. So the best case complexity is O(1).

# Worst Case: In the worst case, the key might be present at the last index i.e., opposite to the end from which the search has started in the list. So the worst-case complexity is O(N) where N is the size of the list.

# Average Case: O(N)



# Binary Search

# To apply Binary Search algorithm:
# The data structure must be sorted.
# Access to any element of the data structure should take constant time.


# The Binary Search Algorithm can be implemented in the following two ways

# Iterative Binary Search Algorithm
# Recursive Binary Search Algorithm


# Iterative Binary Search Algorithm
# Here we use a while loop to continue the process of comparing the key and splitting the search space in two halves.

# Code

def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:

        mid = low + (high - low) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        else:
            high = mid - 1

    # If we reach here, then the element
    # was not present
    return -1

if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10

    result = binarySearch(arr, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")
        
        

# Output
# Element is present at index 3

# O(log n) Time and O(1) Space



#Recursive Binary Search Algorithm:
# Create a recursive function and compare the mid of the search space with the key. And based on the result either return the index where the key is found or call the recursive function for the next search space.

# Code

def binarySearch(arr, low, high, x):

    # Check base case
    if high >= low:

        mid = low + (high - low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, low, mid-1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, high, x)

    # Element is not present in the array
    else:
        return -1

if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10
    
    result = binarySearch(arr, 0, len(arr)-1, x)
    
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")
        

# Output
# Element is present at index 3


# Time Complexity: 
# -> Best Case: O(1)
# -> Average Case: O(log N)
# -> Worst Case: O(log N)

# Auxiliary Space: O(1), If the recursive call stack is considered then the auxiliary space will be O(log N).