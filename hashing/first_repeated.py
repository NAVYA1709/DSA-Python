# Problem: First Repeated Element
# Approach: Check dictionary while traversing
# Time Complexity: O(n)

nums = [5,3,4,3,2]
dic = {}
for num in nums :
    if num in dic :
            print(num)
            break
    else :
        dic[num]=1
