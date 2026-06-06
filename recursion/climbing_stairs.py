# Problem: Climbing Stairs
# Approach: Dynamic Programming (Fibonacci Pattern)
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def climbStairs(self, n):
        if n == 0 or n == 1:
            return 1
        a = 1
        b = 1
        for i in range(2, n + 1):
            c = a + b
          
            a = b
            b = c
        return b
