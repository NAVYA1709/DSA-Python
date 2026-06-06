# Problem: Reverse Number using Recursion
# Approach: Extract last digit and build reverse
# Time Complexity: O(n)
# Space Complexity: O(n)

def reverse(n, rev):
    if n == 0:
        return rev
    digit = n % 10
    rev = rev * 10 + digit
    return reverse(n // 10, rev)

print(reverse(1234, 0))
