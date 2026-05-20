# Problem: Reverse String
# Approach: Traverse string backward and build new string
# Time Complexity: O(n)

word = "python"
rev_word = ""
for i in range(len(word)-1,-1,-1) :
    rev_word+=word[i]
print(rev_word)
if word == rev_word :
    print("Palindrome!!")
else :
    print("Not a palindrome")
