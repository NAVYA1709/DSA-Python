# Problem: Linear Search
#Time Complexity : O(n) 

def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1
