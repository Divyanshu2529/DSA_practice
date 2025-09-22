# Strings 

# In Python, a string is a sequence of characters enclosed in quotes. It can include letters, numbers, symbols or spaces. Since Python has no separate character type, even a single character is treated as a string with length one. Strings are widely used for text handling and manipulation.


# Creating a String

s1 = 'GfG'  # single quote
s2 = "GfG"  # double quote
print(s1)
print(s2)

# Output
# GfG
# GfG



# Multi-line Strings
# Use triple quotes ('''...''' ) or ( """...""") for strings that span multiple lines. Newlines are preserved.

s = """I am Learning
Python String on GeeksforGeeks"""
print(s)

s = '''I'm a 
Geek'''
print(s)

# Output
# I am Learning
# Python String on GeeksforGeeks
# I'm a 
# Geek

# Accessing characters in String

s = "GeeksforGeeks"
print(s[0])   
print(s[4])

# Output
# G
# s

# String Slicing
s = "GeeksforGeeks"
print(s[1:4])    
print(s[:3])     
print(s[3:])     
print(s[::-1])   

# Output
# eek
# Gee
# ksforGeeks
# skeeGrofskeeG



#String Iteration : strings are iterable; you can loop through characters one by one.

s = "Python"
for char in s:
    print(char)
    

# Output
# P
# y
# t
# h
# o
# n



#Deleting a String
s = "GfG"
del s



#Updating a String
s = "hello geeks"
s1 = "H" + s[1:]                   
s2 = s.replace("geeks", "GeeksforGeeks")  
print(s1)
print(s2)

# Output
# Hello geeks
# hello GeeksforGeeks



# Concatenating and Repeating Strings
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)

#Output
# Hello World


# We can repeat a string multiple times using * operator.

s = "Hello "
print(s * 3)

# Output
# Hello Hello Hello 


# Using f-strings
name = "Alice"
age = 22
print(f"Name: {name}, Age: {age}")

# Output
# Name: Alice, Age: 22


# 1. len(): The len() function returns the total number of characters in a string (including spaces and punctuation).

# Example:

s = "GeeksforGeeks"
print(len(s))

# Output
# 13


# 2. upper() and lower(): upper() method converts all characters to uppercase whereas, lower() method converts all characters to lowercase.

# Example:
s = "Hello World"
print(s.upper())
print(s.lower())

# Output
# HELLO WORLD
# hello world


# 3. strip() and replace(): strip() removes leading and trailing whitespace from the string and replace() replaces all occurrences of a specified substring with another.

# Example:
s = "   Gfg   "
print(s.strip())    

s = "Python is fun"
print(s.replace("fun", "awesome"))


# Output
# Gfg
# Python is awesome


# String Membership Testing


s = "GeeksforGeeks"
print("Geeks" in s)
print("GfG" in s)


# Output
# True
# False




# Check if two strings are same or not

# Approach - By Using (==) in C++/Python/C#

def areStringsSame(s1, s2):
    return s1 == s2

if __name__ == '__main__':
    s1 = "abc"
    s2 = "abcd"

    # Call the areStringsSame function to compare strings
    if areStringsSame(s1, s2):
        print("Yes")
    else:
        print("No")
        
        

# Output
# No

# Time Complexity: O(n)
# Auxiliary Space: O(1)



# Approach - By Writing your Own Method

# In this approach, the program compares two strings by first checking if their lengths are the same. If the lengths differ, the strings cannot be identical, so it returns false. If the lengths are the same, it then compares each character of the two strings one by one. If any mismatch is found, it returns false, indicating the strings are not the same. If no differences are found throughout the comparison, it returns true, meaning the strings are identical.


def are_strings_equal(s1, s2):
    # Compare lengths first
    if len(s1) != len(s2):
        return False

    # Compare character by character
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False

    return True

s1 = "hello"
s2 = "hello"

if are_strings_equal(s1, s2):
    print("Yes")
else:
    print("No")
    
    
# Output
# Yes
# Time Complexity: O(n)
# Auxiliary Space: O(1)




# Program to Search a Character in a String

# Approach - By Using in-built library functions

def find_character_index(s, ch):
    idx = s.find(ch)
    return idx 

s = "geeksforgeeks"
ch = 'k'

index = find_character_index(s, ch)
print(index)

# Output
# 3

# O(n) Time and O(1) Space


# Approach - By traversing the string 
def findChar(s, ch):
    n = len(s)
    for i in range(n):
      
        # If the current character is equal to ch, 
        # return the current index
        if s[i] == ch:
            return i

    # If we did not find any occurrence of ch,
    # return -1
    return -1

if __name__ == "__main__":
    s = "geeksforgeeks"
    ch = 'k'
  
    print(findChar(s, ch))
    
# Output
# 3

# (n) Time and O(1) Space



# Insert a character in String at a Given Position

# [Approach-1] Using Built-In Methods
def insertChar(s, c, pos):
  
    # Insert character at specified position
    return s[:pos] + c + s[pos:]

s = "Geeks"
print(insertChar(s, 'A', 3))


# Output
# GeeAks

# Time Complexity: O(n) where n is the length of the string.



# [Approch-2] Using Custom Method
def insertChar(s, c, pos):
    res = ""
    for i in range(len(s)):
      
        # Insert the character at 
        # the given position
        if i == pos: 
            res += c
      
        # Insert the original characters
        res += s[i]
  
    # If the given pos is beyond the length,  
    # append the character at the end
    if pos >= len(s): 
        res += c
      
    return res

s = "Geeks"
print(insertChar(s, 'A', 3))


# Output
# GeeAks

# Time Complexity: O(n) where n is the length of the string.




# Remove a Character from a Given Position

# Approach - By Using Built-In Methods
def remove_char_at_position(s, pos):
    if pos < 0 or pos >= len(s):
        return s
    return s[:pos] + s[pos+1:]

s = "abcde"
pos = 1
print("Output:", remove_char_at_position(s, pos))

# Output
# Output: acde

# Time Complexity: O(n)
# Auxiliary Space: O(1)



# Approach - By Writing Your Own Method

def remove_char_at_position(s, pos):
  
    # Check for valid position
    if pos < 0 or pos >= len(s): 
        return s

    # Convert string to list for mutable operations
    s_list = list(s)  
    
    # Shift characters to the left from the position
    for i in range(pos, len(s) - 1):
        s_list[i] = s_list[i + 1]

    # Remove the last character
    s_list.pop()  
    
    return ''.join(s_list) 
  
s = "abcde" 
pos = 1 
s = remove_char_at_position(s, pos)  
print(s)



# Output
# acde

# Time Complexity: O(n)
# Auxiliary Space: O(1)






# Remove all occurrences of a character in a string

#  Using Built-In Methods

s = "ababca"
c = 'a'

# Remove all occurrences of 'c' from 's'
s = s.replace(c, '')

print(s)

# Output
# bbc


# Writing Your Own Method
def remove_char(s: str, c: str) -> str:
    result = []
    for ch in s:
        if ch != c:
            result.append(ch)
    return "".join(result)

def main():
    s = "geeksforgeeks"
    s = remove_char(s, 'g')
    print(s)

if __name__ == "__main__":
    main()

# Output
# eeksforeeks

# Time Complexity : O(n) where n is length of input string.
# Auxiliary Space : O(1)



# Concatenation of Two Strings

s1 = "Hello, "
s2 = "World!"

# Concatenating the strings
res = s1 + s2

print(res)

# Output
# Hello, World!

# Write your Own Method
def concat(s1, s2):
    res = ''
    
    # Append s1 to res
    for c in s1:
        res += c
    
    # Append s2 to res
    for c in s2:
        res += c
    
    return res

if __name__ == '__main__':
    s1 = 'Hello, '
    s2 = 'World!'
    
    # Call the function to concatenate the strings
    res = concat(s1, s2)
    
    print(res)
    


# Output
# Hello, World!

# Time Complexity : O(m + n) where m and n are lengths of the two strings.






#Reverse a String
# Using backward traversal 

def reverseString(s):
    res = []
  
    # Traverse on s in backward direction
    # and add each character to the list
    for i in range(len(s) - 1, -1, -1):
        res.append(s[i])

    # Convert list back to string
    return ''.join(res)

if __name__ == "__main__":
    s = "abdcfe"
    print(reverseString(s))
    

# Output
# efcdba

# Time Complexity: O(n) for backward traversal
# Auxiliary Space: O(n) for storing the reversed string.
    


# Using Two Pointers 

def reverseString(s):
    left = 0
    right = len(s) - 1
    
    # Convert string to a list for mutability
    s = list(s)  
    
    # Swap characters from both ends till we reach
    # the middle of the string
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    
    # Convert list back to string
    return ''.join(s)  

if __name__ == "__main__":
    s = "abdcfe"
    print(reverseString(s))
    

# Output
# efcdba

# Time Complexity: O(n) 
# Auxiliary Space: O(1)



#  Using Recursion
# Python program to reverse a string using Recursion

# Recursive Function to reverse a string
def reverseStringRec(arr, l, r):
    if l >= r:
        return

    # Swap the characters at the ends
    arr[l], arr[r] = arr[r], arr[l]

    # Recur for the remaining string
    reverseStringRec(arr, l + 1, r - 1)

def reverseString(s):
  
  	# Convert string to list of characters
    arr = list(s)  
    reverseStringRec(arr, 0, len(arr) - 1)
    
    # Convert list back to string
    return ''.join(arr)  

if __name__ == "__main__":
    s = "abdcfe"
    print(reverseString(s))
    
    
# Output
# efcdba

# Time Complexity: O(n) where n is length of string
# Auxiliary Space: O(n)


# Using Stack - O(n) Time and O(n) Space

# Python program to reverse a string using stack
def reverseString(s):
    stack = []
    
    # Push the characters into stack
    for char in s:
        stack.append(char)

    # Prepare a list to hold the reversed characters
    rev = [''] * len(s)

    # Pop the characters from stack into the reversed list
    for i in range(len(s)):
        rev[i] = stack.pop()

    # Join the list to form the reversed string
    return ''.join(rev)

if __name__ == "__main__":
    s = "abdcfe"
    print(reverseString(s))
    
    
# Output
# efcdba

# Time Complexity: O(n) 
# Auxiliary Space: O(n)


# Using Inbuilt methods 

# Function to reverse a string
def reverseString(s):
  	
    # Reverse the string using slicing
    return s[::-1]

if __name__ == "__main__":
    str = "abdcfe"
    print(reverseString(str))
    
    

# Output
# efcdba

# Time Complexity: O(n)
# Space Complexity: O(1)





# Generate all Sunstrings

# [Expected Approach] - Using Iteration
# Function to find all substrings
def find_substrings(s):
    
    # to store all substrings
    res = []
    for i in range(len(s)):
        for j in range(i, len(s)):
            res.append(s[i:j+1])
    return res

s = 'abc'
res = find_substrings(s)
for i in res:
    print(i, end=' ')
    
    
# Output
# a ab abc b bc c 



# [Interesting Approach] - Using Recursion
# Python program to find all the
# substrings of given string

# Recursive Function to find all
# substrings of a string
def subString(s, n, index, cur, res):

    # if we have reached the
    # end of the string
    if index == n:
        return

    # add the character s[index]
    # to the current string
    cur += s[index]

    # add the current string in result
    res.append(cur)

    # move to next index
    subString(s, n, index + 1, cur, res)

    # remove the current character
    # from the current string
    cur = cur[:-1]

    # if current string is empty
    # skip the current index to
    # start the new substring
    if not cur:
        subString(s, n, index + 1, cur, res)

# Function to find all substrings
def findSubstrings(s):

    # to store all substrings
    res = []

    # to store current string
    cur = ""
    subString(s, len(s), 0, cur, res)
    return res

if __name__ == "__main__":
    s = "abc"
    res = findSubstrings(s)
    print(" ".join(res))
    


# Output
# a ab abc b bc c 