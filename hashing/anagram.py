# Problem: Valid Anagram
# Approach: Character frequency counting using dictionary
# Time Complexity: O(n)
# Space Complexity: O(n)
    word1 = "listen"
    word2 = "silent"

    freq1 = {}
    freq2 = {}

    for ch in word1:
        if ch in freq1:
            freq1[ch] += 1
        else:
            freq1[ch] = 1

    for ch in word2:
        if ch in freq2:
            freq2[ch] += 1
        else:
            freq2[ch] = 1

    if freq1 == freq2:
        print("Anagram")
    else:
        print("Not anagram")
