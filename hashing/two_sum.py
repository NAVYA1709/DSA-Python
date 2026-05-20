# Problem: Two Sum
# Approach: Store visited numbers in dictionary for fast lookup
# Time Complexity: O(n)

class Solution(object):
    def twoSum(self, nums, target):
        dic = {}

        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in dic:
                return (dic[needed],i) # old index, current index(cleaner)

            dic[nums[i]] = i
