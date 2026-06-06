# Problem: Word Frequency Counter
# Approach: Using split()
# Time Complexity: O(n)
# Space Complexity: O(n)
sentence = "I   love   python"
words = sentence.split()
print(len(words))

# .split() -> handles ALL whitespace smartly.
