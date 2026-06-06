# Problem: Stack Basics using List
# Operations: Push, Pop, Peek
# Time Complexity:
# Push  -> O(1)
# Pop   -> O(1)
# Peek  -> O(1)

stack = []

# Push
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack after push:", stack)

# Pop
removed = stack.pop()
print("Removed element:", removed)

# Peek
print("Top element:", stack[-1])

# Display stack
print("Final stack:", stack)
