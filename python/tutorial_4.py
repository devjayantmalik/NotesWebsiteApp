# ==================================================
# ==================================================
#               String functions
# ==================================================
# ==================================================






# Create a string variable with whitespaces in it
# Remove whitespaces from left side
# Remove whitespaces from right side
# Remove whitespaces from both sides
# Capitalize first letter of the string
# Convert whole string to uppercase
# Convert whole string to lowercase
# Convert a list of words to string seperated by spaces
# Convert a string into a list
# Count word occurence in a string
# Retrieve index of matching word in a string
# Replace words inside of string


# Create a string with whitespaces
str = "    this is a string with whtiespaces       "

# Remove whitespace from left side
print("String without left whitespace:", str.lstrip())

# Remove whitespace from right side
print("String without right whitespace:", str.rstrip())

# Remove whitespace from both sides
print("String without whitespace:", str.strip())

# For further action removing whitespace from string
str = str.strip()

# Capitalize first letter of string
print("Capitalized string:", str.capitalize())

# Convert whole string to lowercase
print("Uppercase string:", str.upper())

# Convert whole string to uppercase
print("lowercase string:", str.lower())

# convert a list of words to string
listOfWords = ['Jayant', 'Malik', 'is', 'a', 'programmer']
result = " ".join(listOfWords)

# Print result
print("list converted to string:", result)

# Convert a string into a list of words
listOfWords = []
listOfWords = str.split()

# Printing list of words
print("string to list of words:", listOfWords)

# Count a word occurence in a string
print("no. of words in a string:", str.count("is"))

# Retrieve index of matching word in a string
print("is is at index:", str.find("is"))

# Replace words inside of string
print("is replaced with:", str.replace("is", "with"))


# ============================================
# Create an acronym generator:
# The words in resultant acronym must be uppercase

# Sample output:
# Enter a bunch of words to calculate acronymm: Random Access Memory
# Acronymm: RAM


# Ask the user for complete string to generate acronym
userWords = input("Enter a bunch of words to generate acronymm: ")

# Convert the user entered words in a list
list = []

# Add string into the list
list = userWords.split()

# Create a variable to hold acronym
acronym = ""
# Navigate through the list and get first letter of the each item
for item in list:
    acronym += item[0].upper()

print("Acronym:", acronym)


# ===================================================
# Check if a string is alphabet
# Check if a string is alphabetic or numeric (alphanumeric)
# Check if a string is a space
# Check if a string is a numeric
# Check if a string is a decimal
# Check if a string is a digit
# Check if a string is an identifier
# Check if a character is printable
# Check string case: title, upper, lower


# Check if a string is character
print("is 'ABC' alphabet:", "ABC".isalpha())

# Check if a string is alphanumeric
print("is 'ABC5' alphanumeric:", "ABC4".isalnum())

# Check if a string is a space
print("is ' ' a space:", " ".isspace())

# Check if a string is a numeric
print("is '423' is number:", "423".isnumeric())

# Check if a string is a decimal
print("is '34.32' a decimal:", "34.32".isdecimal())

# Check if a string is a digit
print("is '25' a digit:", "25".isdigit())

# Check if a string is an identifier
print("is '-' an identifier:", "-".isidentifier())

# Check if a character is printable
print("is '\\0' printable:", "\0".isprintable())

# Check string case: title, upper, lower
print("is 'Word' title case:", "Word".istitle())
print("is 'WORD' upper case:", "WORD".isupper())
print("is 'data' lower case:", "data".islower())


# ===================================================
# Create a function to check if a number if float
# Use exception handling in the function

def isfloat(str):
    try:
        float(str)
        return True
    except:
        return False

print("is 3.14 a float:", isfloat(3.14))


# ======================================================
# Create a Caesar cipher. Encryption program

# Rules:
# Do not change any character if it is not a letter. Keep it as it is.
# Ask the user for no of characters to shift.

# Algorithm:
# Any letter that is entered shifts n position as entered by the user.
# if user enters 3 then
# A becomes D, B becomes E

# Unicodes for character:
# A - Z : 65 - 90
# a - z : 97 - 122


# Ask the user for message and no of characters to shift
message = input("Enter message: ")
key = int(input("Enter no of position to shift: "))

# Prepare the secret_message
encodedCode = ""
decodedCode = ""

# mechanism for encoding
for character in message:
    if character.isupper():
        encodedCode += chr(((ord(character) + key - 65) % 26) + 65)

    elif character.islower():
        encodedCode += chr(((ord(character) + key - 97) % 26) + 97)


    else:
        encodedCode += character


# mechanism for decoding
for character in encodedCode:
    if character.isupper():
        decodedCode += chr(((ord(character) - key - 65) % 26) + 65)

    elif character.islower():
        decodedCode += chr(((ord(character) - key - 97) % 26) + 97)


    else:
        decodedCode += character


# Print encoded and decoded
print("Encrypted Message:", encodedCode)
print("Decrypted Message:", decodedCode)



# =========================================================
# Create a Caesar cipher. Encryption program by seperating code in functions
def encrypt_message(message, key):
    # Create a variable to store code
    code = ""

    for character in message:
        if character.isupper():
            code += chr(((ord(character) + key - 65) % 26) + 65)

        elif character.islower():
            code += chr(((ord(character) + key - 97) % 26) + 97)


        else:
            code += character


    return code

def decrypt_message(message, key):
    # Create a variable to store code
    code = ""

    for character in message:
        if character.isupper():
            code += chr(((ord(character) - key - 65) % 26) + 65)

        elif character.islower():
            code += chr(((ord(character) - key - 97) % 26) + 97)


        else:
            code += character


    return code


def main():
    # Ask user for input
    message = input("Enter message: ")
    key = int(input("Enter no of characters to shift: "))

    # Encrypt message
    encrypted = encrypt_message(message, key)

    # Decrypt message
    decrypted = decrypt_message(encrypted, key)

    # Print the encrypted message
    print("Encrypted Message:", encrypted)
    print("Decrypted Message:", decrypted)



if __name__ == '__main__':
    main()