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
