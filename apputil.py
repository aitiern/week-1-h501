# Import Libraries 
import string
import re

# Exercise 1
def palindrome(word):
    # Remove spaces and punctuation, keep only letters and numbers
    cleaned = "".join(
        ch.lower() for ch in word 
        if ch.isalnum()
    )
    
    # Check if string equals its reverse
    return cleaned == cleaned[::-1]

# --- Examples ---
print(palindrome("Racecar"))                           # True
print(palindrome("A man, a plan, a canal: Panama!"))   # True
print(palindrome("No lemon, no melon"))                # True
print(palindrome("Hello, world!"))                     # False
print(palindrome("12321"))                             # True
print(palindrome("12345"))                             # False

# Exercise 2
# Method 1: Single-pass counter (this is one going to output faster, ignores non-paren chars)
def parentheses(seq: str) -> bool:
    c = 0
    for ch in seq:
        if ch == '(':
            c += 1
        elif ch == ')':
            c -= 1
            if c < 0:   # early exit if a close appears before an open
                return False
    return c == 0

# Method 2: Pair-elimination (iteratively remove "()" until none remain)
# Also ignores non-paren chars. Simpler to read, but O(n^2) worst-case.
def parentheses_alt(sequence):
    s = ''.join(ch for ch in sequence if ch in '()')
    while '()' in s:
        s = s.replace('()', '')
    return s == ''


# --- Test Cases ---
tests = [
    "((blah)()()())",   # True
    "(((())blee))",     # True
    "(()hello((())()))",# True
    "((((((())",        # False
    "()))",             # False
]

for t in tests:
    print(t, "->", parentheses(t), "/", parentheses_alt(t))

# Lab Exploration 1

def findLargestNumber(words):
    # filter words that are purely digits
    numbers = [int(word) for word in words if re.match(r"\d+", word)]
    # if there are numbers, return the largest
    if numbers:
        return sorted(numbers, reverse=True)[0]
    else:
        return None

print(findLargestNumber(aiw_words))  # Output: 100
