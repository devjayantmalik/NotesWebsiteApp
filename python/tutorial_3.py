# ==================================================
# ==================================================
#               Maths, string
# ==================================================
# ==================================================


# # Ask the user to enter a number:
# # if user enters some character or string then handle the error
# # and force the user to enter a number.
#
# while True:
#     # Try to do some action
#     try:
#         # Ask the user to enter a number.
#         number = int(input("Enter a number: "))
#         # If number is entered then break the loop
#         break
#     # If invalid value is passed then value error occurs
#     except ValueError:
#         print("You entered an invalid number.")
#
#     except:
#         print("An unknown error occured.")
#
# print("Thank you for entering a number.")
#
# # Create a guessing game(simulation of do while loop):
# # Note: do while loop does not exist in python.
# # ========================
# # Guess a number between 1 and 10: 1
# # If the above input is incorrect then prompt again.
# # Guess a number between 1 and 10: 7
# # Use random module to generate a number.
# # You got it right.
#
# import random
#
# # Machine generates a lucky number
# luckyNumber = random.randrange(1,11)
#
# # User enters a number:
# userNumber = -1
#
# while True:
#     # Check if guessed and entered number are correct.
#     if luckyNumber == userNumber:
#         print("You guessed it right.")
#         break
#     # Prompt user for entering a number again.
#     else:
#         userNumber = int(input("Enter a number: "))
#
#

# =================================================
# Using math functions available in math module
# Print special values e and pi available in math module
# Calculate:
# ceil(4.4) : round values to next full int, that is 4.1...4.9 becomes 5
# floor(4.4) : round values to previous full int, that is 4.1...4.9 becomes 4
# fabs(-4.4) : gets absolute value, means removes negative sign

# factorial(4) : Equivalent to 1 * 2 * 3 * 4
# fmod(5,4) : float modulus - Remainder of the division
# trunc(4.2) : truncate - Receive a float and returns an int
# pow(2,3) : raises 2 to the power of 3, that is 2 * 2 * 2
# sqrt(4) : Calculates square root of the number.
# exp(3) : returns e to the power of 3
# log(20) : returns natural logarithm, that is e * e * e ~= 20, so log(20) tells e^3 ~= 20
# log(1000, 10) : allows to define base and 10^3 equals 1000
# log10(1000) : use of base 10 to calculate log.

# Trignometric functions:
# sin, cos, tan, asin, acos, atan, atan2, asinh, acosh, atanh, sinh, cosh, tanh
# The trignometric functions ending with h are known as hyperbolic fuctions in math.

# Convert radians to degrees and vice versa
# degrees(1.5708): returns number after converting to degrees.
# radians(90) : returns number after converting to radians.

# =========================================
# Performing more accurate calculations using decimal module
# Use from moduleName import className as anyVariable
# Perform the calculation: (0.1 + 0.1 + 0.1) - 0.3
# Also print type of sum variable used to store decimal

from decimal import Decimal as D

# Creating a decimal object and storing initial value to it
sum = D(0)

# Adding value to sum
sum += D("0.1")
sum += D("0.1")
sum += D("0.1")

# Subtracting value from sum
sum -= D("0.3")

# Print value to output. The result is 0.0 even after 100 decimal points.
print("(0.1 + 0.1 + 0.1) - 0.3 Equals: {:.100f}".format(sum))

# Print type of sum variable
print(type(sum))

# ===============================================================================
# Create three different variables and find the data type of each variable
# Create an :
# Integer variable
# floating variable
# Boolean variable. True and False start with capital letter in case of booleans
# string variable
# Note: character data type do not exist in python

# Integer variable
num1 = 10
# floating variable
num2 = 20.4
# Boolean variable. True and False start with capital letter in case of booleans
isAlive = True

# Both are strings characters data type do not exist in python
str1 = "Data 1"
str2 = 'Data 2'

print("10 is an", type(num1))
print("20.4 is an", type(num2))
print("isAlive is an", type(isAlive))
print("str1 is an", type(str1))
print("str2 is an", type(str2))

# =================================================================
# Create a string
# Find length of the string.
# Access elements of a string using indexes,(while loop)
# Access elements of a string using for loop
# Access last element of the string using indexes
# Slice a string: string[start:end] means create a string from start index to end index excluding last
# String Concatenation using + symbol
# String multiplication : repeat of string using * symbol
# Conversion of string to unicode using ord()
# Conversion of unicode to string using chr()


# Declaring a string
sampleString = "The peace and war exists in you. - Jayant Malik"


# Access elements of a string using indexes
count = 0
length = len(sampleString)
while count < length:
    print("[{}] = {}".format(count, sampleString[count]))
    count += 1

# Access characters of string using for loop
for character in sampleString:
    print(character, end=" ")

print()

# Print last two elements of a string using index syntax
print('Last Item: ', sampleString[-1])
print("Last Second Item: ", sampleString[-2])

# Slicing a string
print("Sliced String:",sampleString[0:9])

# Concatenating a string using + symbol
data = "Jayant" + " is a software developer."
print(data)

# Multiplication of string
data = "This is my code. " * 5
print(data)

# Conversion of unicode to string
print("A =", ord("A"))

# Conversion of string to unicode
print("65 =", chr(65))


# ============================================================
# Receive a uppercase string and then hide its meaning by
# turing it meaning into a string of unicodes
# Then translate unicode back to its original meaning.
# Sample :
# Enter a string to hide in uppercase: HIDE
# Secret Message: 72736869
# Original Message: HIDE

# Recommendations:
# Use for loop to convert unicode back to string.

# Ask the user to enter a message to hide
originalMessage = input("Enter a string to hide in uppercase: ")

# Creating a variable to store unicode of originalMessage
secretMessage = ""

for character in originalMessage:
    secretMessage += str(ord(character))

# Print Secret message on screen
print("Secret Message:", secretMessage)

# Print original message
print("Original Message:", originalMessage)

# Printing original message using for loop
newMessage = ""
for i in range(0, len(secretMessage)-1, 2):
    secretCode = chr(int(secretMessage[i]+secretMessage[i+1]))
    newMessage += secretCode

print("Original Message:", newMessage)

# ============================================================
# Receive a uppercase or lowercase string and then hide its meaning by
# turing it meaning into a string of unicodes
# Then translate unicode back to its original meaning.
# Sample :
# Enter a string to hide: Hide
# Secret Message: 72105100101
# Original Message: Hide

# Recommendations:
# Use for loop to convert unicode back to string.


# Ask user for message to encrypt
message = input("Enter message to encrypt: ")

# Process secretCode and originalMessage
secretCode = ""
originalMessage = ""

# Cycle through each character of message
for character in message:

    # If unicode of a character is less than 100
    if ord(character) < 100:

        # add a zero before the character unicode
        secretCode += "0"+ str(ord(character))

    # else
    else:

        # add the unicode of character to secretCode
        secretCode += str(ord(character))

# Convert secret code back to characters and print them
for i in range(0, len(secretCode) - 1, 3):

    # Extract first 3 characters form secret code and convert back to int
    code = int(secretCode[i] + secretCode[i+1] + secretCode[i+2])

    # Add chars to secretMessage
    originalMessage += chr(code)

# Print secret message on screen
print("Secret message: {}".format(originalMessage))