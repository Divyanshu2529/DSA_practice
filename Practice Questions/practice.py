# Array and Hashing

# Two Sum

# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         seen={}
#         for i in range(len(nums)):
#             ele = nums[i]
#             diff = target - ele
#             if diff in seen:
#                 return[seen[diff],i]
#             seen[ele] = i
            
            
# Hashing pattern - made an empty hash Table (empty dict) and iterate through the array and get the difference by subtracting target - element if the diff in hash Table return the index the difference is in, otherwise keep appending the element as key and and index of it as value.
            
            
# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]







# Longest Substring Without Repeating Characters

# Sliding Window- to calculate the length of window the formula always gonna be W = (R-L)+1, This question is the Variable length version example


