

"""
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        dic = dict()
        for i, val in enumerate(nums):
            if target - val in dic:
                return [dic[target-val], i+1]
            dic[val] = i+1

class Solution1:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        dic = dict()
        i=0
        for num in nums:
            dic[num] = i++

class Solution2:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        dic = dict()
        i=0
        for num in nums:
            dic[num] = i++




nums = [2, 7, 11, 15]
target = 9

s = Solution()
d = s.twoSum(nums, target)

# print d.items()
# return a map, but can not use the items() method, the return is regarded as a list
print d