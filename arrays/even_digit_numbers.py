# Problem: Find Numbers with Even Number of Digits
# Approach: Convert number to string and count digits
# Time Complexity: O(n)

class Solution(object):
    def findNumbers(self, nums):
        count = 0

        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1

        return count
