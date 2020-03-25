# ==================================================
# ==================================================
#               Regular Expression
# ==================================================
# ==================================================

# ===============================
#   LEARN TIME
# [expression]+s? : Get expression and expression with s at last
#   In the above syntax space is not included
# ===============================

# Match zero or one of specific thing
# Create a string : 'cat cats'
# Compile a regular expression to:
# 1. Match all the words that start with letters 'c' 'a' 't'
# 2. cat should be followed by one or more letters
# 3. use ? to mark one or more letters to proceed it.

import re

randStr = 'cat cats'

regex = re.compile('[cat]+s?')

matches = regex.findall(randStr)

for match in matches:
    print(match)


# ===============================
# In the above example replace randStr with : 'doctor doctors doctor's'
# Now write the expression to match all three words in randStr
# Hint: use only: [] + and *


randStr = "doctor doctors doctor's"

# Both the regex will generate same output
regex = re.compile("[doctor]+['s]*")
# regex = re.compile("[doctr]+['s]*?")

matches = regex.findall(randStr)

for match in matches:
    print(match)


# ================================
#       PROBLEM TIME
# ===============================

# Write a single regular expression to find:
# 1. Words in uppercase or lowercase including numbers and _
# 2. Spaces after them
# 3. Then a carriage return (if any)
# 4. Then a newline


sample = '''Just some words
and some more\r
and more
'''

# Import regular expression module
import re

# Compile a regex
regex = re.compile(r"[\w\s]+[\r]?\n")

matches = regex.findall(sample)

for match in matches:
    print(match)


# =========================================
#       Greedy and Lazy Matching
# =========================================
# Greedy Matching:
#   The * or asterisk is called the greedy match because
#   it grabs the biggest expression

# Example of greedy matching is :
# regex = regex.compile('<tag>.*</tag>')
# Outputs in <tag>Some text </tag>

# In the above case the tags were also included in the result.
# This approach is called greedy match.

# In case of lazy matching the output will be:
# only text inside of tags.
# Output: Some text

# To implement lazy matching in the example of greedy match
# just put a ? after the * in the regex


# ==========================================
# Greedy: Grab the largest match possible
# Lazy : Grab the smallest match possible
# ==========================================




# =========================================
# Create a string with opening and closing tags
# and some text between the tags.
# Sample string : '<name>Life on Mars</name><name>Freaks and Geeks</name>'
# 1. Now, write an expression to demonstrate lazy and greedy matching

sample = '<name>Life on Mars</name><name>Freaks and Geeks</name>'

# Greedy approach
regex1 = re.compile('<name>.*</name>')
# lazy approach
regex2 = re.compile('<name>.*?</name>')


matches1 = regex1.findall(sample)
matches2 = regex2.findall(sample)

print("In case of Greedy:")
for match in matches1:
    print(match)

print("In case of Lazy:")
for match in matches2:
    print(match)


# ================================================
#       Word Boundries
# Are used to define where our expression start and end.
# \b is used to define the boundry
# ================================================

# In the string 'ape at the apex' grab only the word ape (not 'ape' of word apex)
sample = 'ape at the apex'

regex = re.compile(r"\bape\b")

matches = regex.findall(sample)

for match in matches:
    print(match)


# ==========================================
#           STRING BOUNDRIES
# Used to extract info between the string
# ^ : Beginning of the string
# $ : Ending of the string
# ==========================================


# Match everything from beginning of the string to the @ symbol (excluding @ symbol)
# Match everything from ending of the string to the @ symbol (excluding @ symbol and space)
# Sample string: 'Match everything up to @'
# Sample string: '@ Get this string'

sample1 = "Match everything up to @"
sample2 = "@ Get this string"

# Grab everything from beginning
regex = re.compile(r"^.*[^@]")

# Grab everything from ending
regex1 = re.compile(r"$.*[^@]")

matches1 = regex.findall(sample1)
matches2 = regex1.findall(sample2)

for match in matches1:
    print(match)

for match in matches2:
    print(match)




