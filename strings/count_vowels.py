# Problem: Count Vowels
# Approach: Traverse string and check vowel membership
# Time Complexity: O(n)

word = "education"
count = 0
for ch in word :
    if ch in "aeiou" :
        count+=1
print(count)
