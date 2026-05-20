# Problem: Count Occurrences
# Approach: Traverse String and count target matches
# Time Complexity: O(n)word = "banana"
word = "banana"
freq = {}
for ch in word :
   if ch in freq :
       freq[ch] += 1 
   else :
       freq[ch] = 1
print(freq)
