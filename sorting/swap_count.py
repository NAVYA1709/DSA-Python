# Problem: Count Swaps in Bubble Sort
# Approach: Increment counter whenever swap happens
# Time Complexity: O(n²)

nums = [5, 3, 8, 1]
swap_count=0
for i in range(len(nums)):
    swapped = False
    for j in range(len(nums)-1) :
        if nums[j] > nums[j+1] :
            swap_count+=1
            swapped = True
            nums[j],nums[j+1]=nums[j+1],nums[j]
    if not swapped:
        break
print(nums) 
print(swap_count)
