# Problem: Reverse String using Stack
# Approach: Push all characters into stack and pop one by one
# Time Complexity: O(n)
# Space Complexity: O(n)

strin="hello"
stack=[]
for l in strin:
    stack.append(l)
print(stack)
reversed=""
for i in range(len(stack)) :
    reversed+=stack.pop()
print(reversed)
