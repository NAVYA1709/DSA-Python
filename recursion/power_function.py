# Problem: Power Function using Recursion
# Approach: Multiply x with power(x, n-1)
# Time Complexity: O(n)
# Space Complexity: O(n)

def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

print(power(2, 5))
