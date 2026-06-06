# Problem: Recursive Binary Search
# Approach: Divide search space recursively
# Time Complexity: O(log n)
# Space Complexity: O(log n)
def binary_search(nums, low, high, target):
    # Base case
    if low > high:
        return -1
    
    mid = (low+high)//2
    if nums[mid] == target :
        return mid
    
     # Search right half
    elif nums[mid] < target :
        return binary_search(nums, mid + 1, high, target)

    # Search left half 
    else :
        return binary_search(nums, low , mid -1 , target)
    
nums = [1, 3, 5, 7, 9, 11]
target = 7
result = binary_search(nums, 0, len(nums) - 1, target)
print(result)   
