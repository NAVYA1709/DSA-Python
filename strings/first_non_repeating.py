# Problem: First Non-Repeating Character
# Approach: Count frequency then find first count = 1
# Time Complexity: O(n)

word = "aabbcde"
freq = {}
for ch in word :
    if ch in freq :
        freq[ch]+=1
    else :
        freq[ch]=1
for key,value in freq.items():
    if value == 1 :
        print(key)
        break
