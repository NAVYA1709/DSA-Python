# Problem: Bubble Sort
# Approach: Compare adjacent elements and swap repeatedly
# Time Complexity: O(n²)
nums = [5, 3, 8, 1]
for i in range(len(nums)):
    for j in range(len(nums)-1) :
        if nums[j] > nums[j+1] :
            nums[j],nums[j+1]=nums[j+1],nums[j]
print(nums)  


# Sort Descending
nums = [5, 3, 8, 1]
for i in range(len(nums)):
    for j in range(len(nums)-1) :
        if nums[j] < nums[j+1] :                #CHANGE
            nums[j],nums[j+1]=nums[j+1],nums[j]
print(nums) 
