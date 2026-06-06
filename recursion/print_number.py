# Problem: Print Numbers using Recursion
# Approach: Recursive call first, then print
# Time Complexity: O(n)
# Space Complexity: O(n)

def print_nums(n):
    if n == 0:
        return
    print_nums(n - 1)
    print(n)
print_nums(5)

#decresing
def print_nums(n) :
    if n ==0:
        return 

    print(n)
    print_nums(n-1)
print_nums(5) 
