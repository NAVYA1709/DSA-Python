# Problem: First and Last Occurrence
# Approach: Traverse list and track matching indices
# Time Complexity: O(n)

# First occurrence
for i in range(len(nums1)):
    if nums1[i] == target_nums1:
        print("Found first at index", i)
        break

# Last occurrence
for i in range(len(nums1)-1, -1, -1):
    if nums1[i] == target_nums1:
        print("Found last at index", i)
        break
