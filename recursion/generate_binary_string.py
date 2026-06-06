# Problem: Generate All Binary Strings
# Approach: Recursively choose 0 and 1
# Time Complexity: O(2^n)
# Space Complexity: O(n)

def generate_binary(n, s):
    if n == 0:
        print(s)
        return
    generate_binary(n - 1, s + "0")
    generate_binary(n - 1, s + "1")

generate_binary(3, "")
