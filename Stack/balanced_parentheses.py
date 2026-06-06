# Problem: Balanced Parentheses
# Approach: Use stack
# Time Complexity: O(n)
# Space Complexity: O(n)


s = "({[]})"
stack = []
valid = True
for ch in s:
    if ch in "({[":
        stack.append(ch)
    else:
        if not stack:               #if stack is empty 
            valid = False
            break
        top = stack.pop()
        if ch == ')' and top != '(':
            valid = False
            break
        if ch == '}' and top != '{':
            valid = False
            break
        if ch == ']' and top != '[':
            valid = False
            break
if valid and not stack:
    print("Balanced")
else:
    print("Not Balanced")
