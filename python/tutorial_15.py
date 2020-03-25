# ==================================================
# ==================================================
#               Regular Expression
# ==================================================
# ==================================================

# Regular expressions help to locate a string in a
# large amount of data
# or check whether the input is in email phone ... format
# and so on.
# Basically they help you to operate strings

# Note: module 're' is used for regular expressions

# =========================================
# Write an example to search a word in a string using regex
# Print Info related to word such as: spans, start, end


import re

# Creating variable to store sentence or word
sentence = 'The ape was at the apex'
word = 'ape'

# Create result variable to store result
result = re.search(word, sentence)

# Print info related to word
if result != None:
    print("Word Spans:", result.span())
    print("Word starts at:", result.start())
    print("Word ends at:", result.end())


# ==========================================
# Find all occurences of word in the sentences using regex
# Example string: The ape was at the apex
# Find all words that starts with an ape
# Sample output: ['ape ', 'apex']
# Note: there is space in 'ape' you can use strip() to get rid of it.

# Find the results
result = re.findall('ape.', 'The ape was at the apex.')

for item in result:
    print(item.strip())


# ====================================================
# Generate iterator of 'ape.' words and print the
# length they spans inside of for loop
# Now use span() result to slice the word out of string.

import re

sen = 'The ape was found at the apex'

for item in re.finditer('ape.', sen):
    temp = item.span()
    print("Spans:", temp)

    print("Word from sen:", sen[temp[0]:temp[1]])


# ======================================
print('='* 10)
# ======================================


# ===================================
# Use of square brackets to match specific letters
# Create a string animals with content: 'Cat rat mat pat'
# Find all the words that end with 'at' but starts
# with any of the letters 'crmfp'

animalStr = 'Cat rat mat pat'

allAnimals = re.findall('[crmfp]at', animalStr)

print(allAnimals)

# ===================================================
# Create a string 'Cat rat mat pat'
# Matching the ranges:
# Find all words that starts with any letter between c and m
# or between C and M and ends with at
# Also find all the words that don't start with letter C or 'r'
bus = 'Cat rat mat pat'

for word in re.finditer('[c-mC-M]at', bus):
    temp = word.span()
    print(bus[temp[0]:temp[1]])

for word in re.findall('[^Cr]at', bus):
    print(word)


# =============================================
# Create a string owlFood = 'cat rat mat pat'
# Compile an regex pattern object with pattern '[cr]at'
# Now use mehods of compiled regex pattern object to:
# substitute own in place of matched owlFood

owlFood = 'cat rat mat pat'

regex = re.compile('[cr]at')

result = regex.sub('owl', owlFood)

print(result)


# =====================================
# Solving the backslahes problem
# find a word \\stuff
# Use search() method to solve the problem
# Also use raw string

tempStr = 'Here is the \\stuff'

print('Result:', re.search(r'\\stuff', tempStr))

# =====================================
# Matching the period character
# Create a string orgs = 'F.B.I. I.R.S. CIA'
# Find no of words that match the pattern:
# Anything followed by a dot then
# anything followed by a dot then
# anything followed by a dot
# Use len()

orgs = 'F.B.I. I.R.S. CIA'

print("Occurences:", len(re.findall('.\..\.', orgs)))


# ===================================
# Match a whitespace
# Create a multiline string
# Use regex compile pattern to find the result
# Replace all new lines from the string with a space

randStr = '''This is
a random string
that goes on for many lines
'''

print("Original:", randStr)

regex = re.compile('\n')
randStr = regex.sub(' ', randStr)

print("Result:", randStr)


# ======================================
# LEARN TIME
# \d is same as [0-9]
# \D is same as [^0-9]
# ======================================

# Use of curly braces
# Create a string variable num = '12345'
# 1. Now use regex to match digit occurences in the string num
# 2. After that, count the occurences of digits in pairs.
# Example of 1. 1 is seperate digit then, 2 and so on.. so we get 5 occurences
# Exaple of 2. In case of pair of 2:
# 12 is a pair then 34 is another pair so we get 2 occurences
# In case of pair of 3:
# we get 1 occurences

import re

num = '12345'

print("Matches without pair:", len(re.findall('\d', num)))
print("Matches with pair of 2:", len(re.findall('\d{2}', num)))
print("Matches with pair of 3:", len(re.findall('\d{3}', num)))


# ====================================
# Match pair of values in range of 5 - 7 digits in the string
# string = '123 1234 123456 1234567'

nums = '123 12345 123456 1234567'

print("Matches:", len(re.findall('\d{5,7}', nums)))


# ================================================
# LEARN TIME:
# \w = [a-zA-Z0-9_]
# \W = [^a-zA-Z0-9_]
# ==================================================


# ===================================
# Check if a number is a valid phone number or not
# A valid phone no is in format: '91-929-232-9879'

phNumber = '91-929-232-9879'

if re.search('\w{2}-\w{3}-\w{3}-\w{4}', phNumber):
    print("It is a phone no.")


# ============================================
# Check if a first name is valid or not.
# A valid first name should be between 2 - 20 characters

fName = 'Jayant'

if re.search('[\w]{2,20}', fName):
    print("It is a valid first name.")


# ================================================
# LEARN TIME
# \s = [\f\n\r\t\v]
# \S = [^\f\n\r\t\v]
# =================================================



# ==================================================
# Check for valid first name and last name
# Condition: valid first name and last name: 'Jayant Malik'
# Characters are between 2 to 20 and their is a space between first and last name


if re.search('\w{2,20}\s\w{2,20}', "Jayant Malik"):
    print("It is a valid name")


# =============================
# LEARN TIME
# + SYMBOL MATCHES FOR ONE OR MORE CHARACTERS
# =================================


# ====================================
# Match for a word that starts with a and
# followed by one or more characters

if re.search('a+', 'apple'):
    print("Yes the word starts with a")

print("Matches with a:", len(re.findall('a+', 'ape apple act trial')))


# =====================================
# PRACTICE TIME

# Write a program to check for valid email address from a list
# Rules:
# 1. 1 to 20 lowercase letters and uppercase letters, numbers, and ._%+-
# 2. An @ symbol
# 3. 2 to 20 lowercase letters and uppercase letters, numbers, and .-
# 4. A period
# 5. 2 to 3 lowercase and uppercase letters


emails = ['adam@gmail.com',
          'Veronics232@mail.edu',
          'sam23dongle@wifi.com',
          '@apple.com',
          'db@.com'
         ]

for mail in emails:
    if re.search('[\w._%+-]{1,20}@[\w.-]{2,20}\.[a-zA-Z]{2,3}', mail):
        print(mail, 'is a valid email')
    else:
        print(mail, "is an invalid email")


# ===================================================
#                   REVISION TIME
# ===================================================
"""
import re

if re.search('REGEX', yourString)

print("Matches:", len(re.findall('REGEX', yourString)))

regex = re.compile('REGEX')

yourString = regex.sub('substitution', yourString)

[ ]   : Match what is in the bracket
[^ ]  : Match anything not in the bracket
.     : Match one Character or space
+     : Match one or more characters
\n    : Match new line
\d    : Match any one number
\D    : Anything but a number
\w    : Same as [a-zA-Z0-9_]
\W    : Same as [^a-zA-Z0-9_]
\s    : Same as [\f\n\r\t\v]
\S    : Same as [^\f\n\r\t\v]
{5}   : Match 5 of what preceeds the curly brackets
{5,7} : Match values that are between 5 and 7 in length 
"""
