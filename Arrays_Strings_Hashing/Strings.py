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

