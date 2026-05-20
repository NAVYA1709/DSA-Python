# Problem: Valid Palindrome
# Approach: Remove non-alphanumeric chars, reverse, compare
# Time Complexity: O(n)

class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        rs=""
        for ch in s :
            if not ch.isalnum() :
                s=s.replace(ch,"")
        for i in range(len(s)-1,-1,-1) :
            rs+=s[i]
        if s == rs :
            return True
        else :
            return False


        
