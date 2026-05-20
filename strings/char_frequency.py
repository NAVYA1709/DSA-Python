# Problem: Character Frequency
# Approach: Use dictionary to count character occurrences
# Time Complexity: O(n)

word = "banana"
freq = {}
for ch in word :
   if ch in freq :
       freq[ch] += 1    
   else :
       freq[ch] = 1
print(freq)
