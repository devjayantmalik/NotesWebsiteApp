# ==================================================
# ==================================================
# Reading Writing Files, Tuples, Recursive Functions
# ==================================================
# ==================================================



# Explain few concepts related to Reading Files:
# os module, with statement, open function


# ===============================================
# Open a txt file in write mode and set its encoding to utf-8
# open the above file as myFile reference.
# use write function only for writing.
# Also make sure to close the file

# Write below text each in seperate line :
# Jayant Malik
# Mohit Sharma
# Nripender
# Shaurya Bhatnagar


# Note: write() does not add a new line at the end of text.


# opening the file in write mode with utf-8 encoding as myFile reference
with open('/home/hp/temp/first_file.txt', mode="w", encoding='utf-8') as myFile:

    # write text to the file
    myFile.write('Jayant Malik\nMohit Sharma\n')
    myFile.write('Nripender\nShaurya Bhatnagar')

    # closing the file
    myFile.close()


# =====================================================
# Write a program to open the first_file.txt for reading
# Now, after opening the file, print the contents of the file
# close the file
# Note: use readlines() and readline() and read() function for reading.
# Note: Demonstrate readline() buffer position issue and fix it by changing buffer position.


# Also check the file metadata by opening the file properties
# in file explorer on windows and nautilus on linux.


# opening file in read mode
with open('/home/hp/temp/first_file.txt', mode="r", encoding='utf-8',) as myFile:

    # Reading file contents using readlines() function
    fileContents = myFile.readlines()

    # Reading file contents using readline() function.
    # Note: the below line will not print any output because
    # buffer position has been shifted to last
    fileContents2 = myFile.readline()

    # Changing buffer position
    myFile.buffer.seek(0)

    # Reprinting fileContents2
    fileContents2 = myFile.readline()

    # printing file contents on screen
    print("result of readlines():", fileContents)
    print("result of readline()", fileContents2)


    # closing the file
    myFile.close()


# =============================================================
# Write a program using file handling:
# use open() to open file
# Change postion of buffer using seek()
# use tell() to tell the position of buffer
# use read() to read data from file
# use readline() to read a single line of text
# use readlines() to read all lines of text and return each line as list element
# use write(), writelines() to write data to file
# Check if a file is writable using writable() function
# use close to close the file.

# use closed property to check if a file buffer is closed
# Retrieve file name using name property
# Retrieve file mode using mode property



# use open() to open file
with open('/home/hp/temp/first_file.txt', mode="a+", encoding='utf-8') as myFile:

    # Change postion of buffer using seek()
    myFile.seek(0)

    # use tell() to tell the position of buffer
    myFile.tell()

    # use read() to read data from file
    print("Data using read:", myFile.read())

    # use readline() to read a single line of text
    print("Data using readline:", myFile.readline())

    # use readlines() to read all lines of text and return each line as list element
    print("Data using readlines:", myFile.readlines())

    # use write(), writeline() to write data to file
    myFile.write('Hello')
    myFile.writelines('Hello World')

    # Check if a file is writable
    print("file writable status:", myFile.writable())

    # use close to close the file.
    myFile.close()


# use closed property to check if a file buffer is closed
print("file closed status:", myFile.closed)

# Retrieve file name using name property
print("file name:", myFile.name)

# Retrieve file mode using mode property
print("file mode:", myFile.mode)


# =====================================================================
#               Using os module
# =====================================================================

# Use os module to:
# Rename a file
# Remove a file
# Create a directory
# Change into directory
# Check current working directory
# Change mode of directory
# Remove a directory

import os

# Rename a file
os.rename('/home/hp/temp/first_file.txt', '/home/hp/temp/second_file.txt')

# Remove a file
os.remove('/home/hp/temp/demo.py')

# Create a directory
os.mkdir('/home/hp/temp/python_test')

# Change into directory
os.chdir('/home/hp/temp/python_test')

# Check current directory
print("Current Directory:", os.getcwd())

# Change mode of directory
os.chmod('/home/hp/temp/python_test', mode=777)

# Remove a directory
print("/home/hp/temp/python_test")


# ======================================================
#           Back to files
# ======================================================

# Write a program that displays txt file contents in such format:
# Sample output:
# Line 1 : Jayant Malik
# Line 2 : Mohit Sharma
# Line 3 : Nripender
# Line 4 : Shaurya Bhatnagar

# Use while loop and readline() function to solve the problem
# Trick : figure out how to check if there is no further lines to read using if statement



# Open the file as file reference
with open('/home/hp/temp/second_file.txt', mode='r', encoding='utf-8') as file:

    # Declare a variable to store line number
    lineNum = 1

    # Use while loop to iterate till the file is not completely read.
    while True:
        text = file.readline()

        if not text:
            break

        # print line on the screen
        print("Line {} : {}".format(lineNum, text), end="")

        # Increment lineNum
        lineNum += 1



# =====================================================
# Write a program to cycle through each line:
# and output no of words per line, and average word length per line


with open('/home/hp/temp/second_file.txt', mode='r', encoding='utf-8') as file:

    # Store info related to words
    lineNum = 1

    # Cycle through file contents
    while True:

        # Read contents of the file
        line = file.readline()

        # If no further data is available then exit the loop
        if not line:
            break

        # Variable to store info
        wordsCount = 0
        charsPerWord = 0
        charsInLine = []

        # Cycle through each line:
        for word in line.split():

            # Increment the wordCount by 1
            wordsCount += 1

            # Calculate no of letters in each word:
            for c in word:
                charsPerWord += 1

            # Append the total chars per word to list
            charsInLine.append(charsPerWord)

        # Calculate average from the list charsInLine
        sum = 0
        elements = len(charsInLine)

        for item in charsInLine:
            sum += item

        # Print words per line information
        print("Line {} : Words = {}, Average word length: {}"
              .format(lineNum, wordsCount, int(sum / elements)))

        # Increment the line Number
        lineNum += 1



# ====================================================
#                       Tuples
# ====================================================
# Note: tuples cannot change their values.


# =====================================================
# Create a tuple
# Access the values of tuple using indexes
# Use slice to get first 3 values from the tuple
# Get length of tuple using length function
# Tuple concatenation using + symbol
# Check if a file is inside a tuple
# Print values of tuple using for loop
# Convert a list in tuple
# Convert a tuple into a list
# Get Minimum and maximum value in a tuple




# Create a tuple
fibs = (1, 1, 2, 3, 5, 8, 13, 21)

# Access the values of tuple using indexes
print("First value using index:", fibs[0])

# Use slice to get first 3 values from the tuple
print("Sliced 3 values:", fibs[0: 3])

# Get length of tuple using length function
print("Length of fibs:", len(fibs))

# Tuple concatenation using + symbol
fibs2 = fibs + (0, 0, 0, 0, 0, 0)

# Check if a file is inside a tuple
print("Is 23 in tuple:", 23 in fibs)

# Print values of tuple using for loop
for val in fibs:
    print(val, end=", ")

# Convert a list in tuple
print("List to tuple:", tuple([1, 2, 3, 4, 5]))

# Convert a tuple into a list
print("Tuple to list:", list(fibs))

# Get Minimum and maximum value in a tuple
print("Max value in tuple:", max(fibs))
print("Min value in tuple:", min(fibs))












