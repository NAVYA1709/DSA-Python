# Problem: Most Frequent Character
# Approach: Count frequency and track highest count
# Time Complexity: O(n)

word = "banana"
freq = {}
for ch in word :
   if ch in freq :
       freq[ch] += 1 
   else :
       freq[ch] = 1
print(freq)
highest = 0 
for key,value in freq.items() :
    if highest < value :
        highest = value
        char = key
print(char)
