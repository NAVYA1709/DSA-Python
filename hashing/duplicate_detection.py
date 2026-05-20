# Problem: Duplicate Detection
# Approach: Store seen elements in dictionary
# Time Complexity: O(n)

nums = [1,2,3,4,2]
dic = {}
for num in nums :
    if num in dic :
        print("Duplicate found !")
        break
    dic[num]=1
