# arr = [2, 4, 6, 8, 10]

# prefix[0] = 2
# prefix[1] = 2 + 4 = 6
# prefix[2] = 2 + 4 + 6 = 12
# prefix[3] = 2 + 4 + 6 + 8 = 20
# prefix[4] = 2 + 4 + 6 + 8 + 10 = 30

# prefix = [2, 6, 12, 20, 30]


def prefix_array(arr):
    prefix = [0] * len(arr)   # create array of same length
    prefix[0] = arr[0]        # first element is same
    
    for i in range(1, len(arr)):
        prefix[i] = prefix[i-1] + arr[i]
    
    return prefix

arr = [2, 4, 6, 8, 10]
print(prefix_array(arr))  # [2, 6, 12, 20, 30]
