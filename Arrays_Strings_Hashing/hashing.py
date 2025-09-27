# Hash Table: Hash Function, Sets, and Maps

# Hashing is a technique used in data structures that efficiently stores and retrieves data in a way that allows for quick access.



# Hashing involves mapping data to a specific index in a hash table (an array of items) using a hash function. It enables fast retrieval of information based on its key.

# The great thing about hashing is, we can achieve all three operations (search, insert and delete) in O(1) time on average.

# Hashing is mainly used to implement a set of distinct items (only keys) and dictionaries (key value pairs).

# Example
# List = [11,12,13,14,15]
# H(x) = [x%10]

# 11%10 = 1  12%10 = 2  13%10 = 3  14%10 = 4 15%10 = 5
# Index          0  1   2   3   4    5
# Hash Table =>     11  12 13   14   15

# What is Collision in Hashing?
# When two or more keys have the same hash value, a collision happens.

# What is meant by Load Factor in Hashing?

# The load factor of the hash table can be defined as the number of items the hash table contains divided by the size of the hash table. 
# Load Factor = Total elements in hash table/ Size of hash table 

# Hashing with Chaining Implementation
# The idea is to make each cell of hash table point to a linked list of records that have same hash function value.


# Hash Set : Its a set of value stored at a perticular index, we can perform operations like lookup, add, and remove

# Lookup: *O(1) amortized
# add: O(1) amortized
# delete: *O(1) amortized


# Hash Map: It have all the same fuctionality as a Hash Set, except it can store data.

# In the hash map, the key get map to the values or the data associated with key, and we need to keep in mind that the keys should be hashable, and the value can be anything.

# Lookup: *O(1) amortized
# add: O(1)
# Remove: *O(1) amortized

# Thing which are hashable: Strings, Integers, Tuples (1,2,3)
# Thing which are not hashable: Array, Dictionaries

# Things that are immutable are hashable and things which are not hashable are mutable.



# Hashsets

s = set()    # it wil create a set s

# adding into the set - O(1)

s.add(1)
s.add(2)
s.add(3)
s.add(4)

# lookup if item in set - O(1)

if 1 in s:
    print(True)
    

# Remove item from set - O(1)

s.remove(3)
print (s)


# set construction - O(S) - S is the length of the string

string= "aaaaaaaaaabbbbbbbbbbcccccccceeeeeeee"

sett= set(string)

print (sorted(sett))





# Hashmaps - called Dictionaries in python 

d = {'greg': 1, 'steve':2, 'rob':3}
print(d)

# Add key:val in dictionary: O(1)

d['arsh'] = 4
print(d)

# Check for presence of key in dictionary: O(1)
if 'greg' in d:
    print(True)
    
# Check the value corressponding to a key in a dictionary: O(1)
print(d['greg'])
# Output: 1

# Loop over the key:val pairs of the dictionary: O(n)
for key, val in d.items():
    print(f'{key}:{val}')
    




# Default Dict

from collections import defaultdict

default = defaultdict(int)

print(default[2])




# Counter - count elements of the thing given to it.

from collections import Counter

string = 'aaaaaaaabbbbbbbbbbcccccccdddddddd'

counter = Counter(string)

print(counter)


# In seperate chaning if we want to put more than one element in the same index then we tie them as a linked list, on the other hand i linear probing if there is already an element on the index we want to put are element then it will put it to the next index and if we delete the one before that then we need to mark it as -1 so that we can look for the element which was put on the next index because it was not empty at that time.



# Collision Resolution Techniques 
# 1) Seperate Chaining (Open Hashing)   2) Open Addressing (Closed Hashing)-  Linear Probing, Quadratic probing, Double Hashing


# 1) Separate Chaining - The idea behind Separate Chaining is to make each cell of the hash table point to a linked list of records that have the same hash function value. Chaining is simple but requires additional memory outside the table.

# 2.) Open Addressing - In open addressing, all elements are stored in the hash table itself. Each table entry contains either a record or NIL. When searching for an element, we examine the table slots one by one until the desired element is found or it is clear that the element is not in the table.

# 2.a) Linear Probing - In linear probing, the hash table is searched sequentially that starts from the original location of the hash. If in case the location that we get is already occupied, then we check for the next location.

# Algorithm:

# Calculate the hash key. i.e.  key = data % size
# Check, if  hashTable[key]  is empty 
# store the value directly by  hashTable[key] = data
# If the hash index already has some value then
# check for next index using  key = (key+1) % size
# Check, if the next index is available hashTable[key] then store the value. Otherwise try for next index.
# Do the above process till we find the space.


# 2.b) Quadratic Probing- Step 1 - Empty hash table with range of hash values from 0 to 6 according to the hash function provided.

# Step 2 - The first Key to be inserted is 22 which is mapped to slot 1 (22%7 =1)

# Step 3 - The nect key 30 which is mapped to Slot 2 (30%7 = 2)

# Step 4 - The next key is 50 which is mapped to Slot 1 (50%7 = 1) but the slot 1 is already occupied. So, we will search slot 1+1^2. Again slot 2 is occupied, so we will search cell slot1+2^2 i.e 1+4 =5


# 2.c) Double Hashing - Step 1 - Empty hash table with range of hash values from 0 to 6 according to the hash function provided.

# Step 2 - The first key to be inserted is 27 which is mapped to slot 6 (27%7=6)

# Step 3 - The next key to be inserted is 43 which is mapped to slot 1 (43%7=1)

# Step 4 - The next key is 692 which is mapped to slot 6 (692%7 = 6), but location 6 is already occupied. Using Double hashing,

#hnew = [h1(692)+i*(h2(692))]%7
# =[6+1*(1+692%5)]%7
# 9%7
# 2

# Now, as 2 is an empty slot, so we can insert 692 into 2nd slot.