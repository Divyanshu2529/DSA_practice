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















# Array and String

# Patterns & Questions:

# 🔹 Sliding Window

# Longest Substring Without Repeating Characters

# Sliding Window- to calculate the length of window the formula always gonna be W = (R-L)+1, This question is the Variable length version example


# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         l = 0
#         longest = 0
#         sett = set()
#         n = len(s)
#         for i in range(n):
#             while s[i] in sett:
#                 sett.remove(s[l])
#                 l += 1
#             w = (i - l) + 1
#             longest = max(w, longest)
#             sett.add(s[i])
#         return longest

# Given a string s, find the length of the longest substring without duplicate characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
















# Find All Anagrams in a String

# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.


# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".


# Constraints:

# 1 <= s.length, p.length <= 3 * 104
# s and p consist of lowercase English letters.


# from collections import Counter
# class Solution(object):
#     def findAnagrams(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: List[int]
#         """
#         p_count = Counter(p)
#         s_count = Counter(s[: len(p)])
#         result = []

#         if p_count == s_count:
#             result.append(0)

#         for i in range(len(p), len(s)):
#             s_count[s[i]] += 1
#             s_count[s[i - len(p)]] -= 1

#             if s_count[s[i - len(p)]] == 0:
#                 del s_count[s[i - len(p)]]

#             if s_count == p_count:
#                 result.append(i - len(p) + 1)
#         return result

# Time: O(n)
# Space: O(1)















# Longest Repeating Character Replacement

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.


# def characterReplacement(s: str, k: int) -> int:
#     freq = {}
#     left = 0
#     max_count = 0
#     res = 0

#     for right in range(len(s)):
#         freq[s[right]] = freq.get(s[right], 0) + 1
#         max_count = max(max_count, freq[s[right]])

#         # If too many chars to replace
#         while (right - left + 1) - max_count > k:
#             freq[s[left]] -= 1
#             left += 1

#         res = max(res, right - left + 1)
    
#     return res


# Time: O(n)
# Space: O(1)






