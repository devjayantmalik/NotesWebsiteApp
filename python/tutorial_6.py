# ==================================================
# ==================================================
#    Lists, Bubble sort and List comprehensions
# ==================================================
# ==================================================




# ===============================================
# Create a list with different values
# Generate a list with range() function
# Join two list using + symbol
# Get first item in the list
# Get length of the list
# Slice a list to get first three elements of the list
# Use for loop to print all elements of the list and their indexes
# Find whether a list contains an item using 'in' operator
# Count no of times an item is in the list
# Append an item to the list
# Remove last item from the list



# Create a list with different values
tempList = ["string", 1.45, 40]

# Generate a list with range function
oneToTen = list(range(10))

# List Concatenation
concatenatedList = tempList + oneToTen

# Get first item in the list
first = oneToTen[0]

# Get length of the list
length = len(oneToTen)

# Slice a list to get first 3 elements
newList = oneToTen[0:3]

# Use for loop to print all elements of the list
for item in oneToTen:
    #Get index of an item
    pos = oneToTen.index(item)
    print("{} : {}".format(pos, item))


# Check if a item contains an item
status = "string" in tempList
print("tempList contains string:", status)

# Count no of times an item is in the list
count = tempList.count("string")

# Append an item to the list
tempList.append("myname")

# Remove an last item from the list
tempList.pop()


# =================================================
# Generate a list with random values between 1 and 9
# Now print each element of list seperated by commas in a single line
# Also remove the comma and space after last element of the list while printing


# Import random module
import random

# Create a list
vals = []

# create a loop to run 9 times
for _ in range(9):
    # Generate a random value
    randomValue = random.randrange(1,10)

    # Add value to the list
    vals.append(randomValue)

# Printing elements of the list
for item in vals:
    print(item, end=", ")

# Remove last comma and space from list
print("\b\b")


# ====================================================================
# Create a random list of 10 elements
# Use bubble sort algorithm to sort those values
# Print all elements of the list on screen
# Bubble Sort:
#


# ====================================================================
# Create a random numbers list between 1 and 9 (9 included)
data = list(range(0, 9))

# sort a list in increasing order
data.sort()
print("sorted list:", data)

# sort a list in decreasing order- reverse the list
data.reverse()
print("reverse sort:", data)

# insert an element at some index in the list
data.insert(3, 2)
print("insert 2 at 3rd position in list:", data)

# remove some value from the list
data.remove(7)
print("7 removed from list:", data)

# remove an item from a list at some specific index - pop
data.pop(3)
print("after removal of data from 3rd index:", data)


# ============================================================
# List Comprehensions:
# are a neat way to perform operations on list using shorter code.
# List comprehensions consists of 3 parts:
# Output/body part of loop
# Input part / for loop itself
# predicate part / condition inside body of loop
# ============================================================


# =================================
# Generate a list of squares of number from 1 to 10


# Create a variable to store output list
# Input part : list of [1,2,3,4....10] using for loop
# Output part: num ** 2 or square of no.
squares = [ num ** 2 for num in range(1, 11)]

# Print value of list variable on screen.
print("Squares from 1 to 10:", squares)



# =========================================================
# Create a program to compute power of 2 from 1 to 10
# Solve using list comprehensions

# Compute powers of 2 from 1 to 10
powersOfTwo = [ 2 ** num for num in range(1, 11)]

# Print the result on the screen.
print("Powers of 2:", powersOfTwo)



# ======================================================
# Compute squares of odd numbers between 1 and 10


# Generate a list of nums between 1 and 10
# Check if the no % 2 != 0
# Calculate the square of the number.
oddSquares = [ num ** 2 for num in range(1, 11) if (num % 2) != 0]

# Print the result
print("Odd Squares:", oddSquares)


# ==========================================================
# Generate a list of prime numbers between 1 and 50
# Prime nos are those which are only devisible by 1 and itself
# Use function and list comprehension both


# Create a function to check if a no is prime
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False

    return True


# Generate a list of nos between 1 and 50
# Check using function if no is prime
# Store it in the list num.
primes = [ num for num in range(1, 51) if is_prime(num)]

# Print the result
print("Primes between 1 and 50:", primes)



# ===================================================
# Generate a list of non primes using function and list comprehension


# Check if the no is not prime
nonPrimes = [num for num in range(0, 51) if is_prime(num) == False]

# Print the result on screen
print("Non Primes:", nonPrimes)



# =========================================================
# Create a list of uppercase characters using list comprehension
# and convert them to lowercase using list comprehension
# Unicodes : A - 65, Z - 90

# Generated uppercase letters
uppercaseLetters = [chr(c) for c in range(65, 90)]

# Print uppercase letters
print("Uppercase Letters:", uppercaseLetters)

# Convert uppercase to lowercase
lowercaseLetters = [ item.lower() for item in uppercaseLetters]


# ==========================================================
# create a string variable and assign "Call me at 9073728292"
# Seperate the numeric digits from the list using list comprehensions


# Create a sample variable
sample = "Call me at 9073728292"

# Seperate numeric digits from no
numericDigits = [ int(character) for character in sample if character.isdigit()]

# Print numeric digits
print("Number:", numericDigits)


# ===============================================================
# Generate a multiplication table of 3 using list comprehension

# Generated a list of multiplication table
table = [ (3 * num) for num in range(1, 11)]

# Print the result on screen
print("Multiplication table of 3:", table)





# ============================================================
#           Multi Dimensional List
# ============================================================

# Create a multi-dimensional list that stores this table:
# -----------------
#  0    1   2
#  1    52   43
#  2    53   44
# ------------------
# Now the print the table elements in format of a table


# Creating a multi-dimensional list
tableOne = [
    [0, 1, 2],
    [1, 52, 43],
    [2, 53, 44]
]


# Printing elements of the table
print("TableOne:")
for item in tableOne:

    # Print elements in item list
    for element in item:
        print(element, end="\t")

    # Print a blank line
    print()

print()
print()

# ============================================================
# Create a list of items from 1 to 5 (say listOne)
# Create an another list(multi-dimensional) that stores
# list of power of 2, power of 3, power 4 of each item present in listOne
# Sample Output:
# listOne: 1, 2, 3, 4, 5
# # listTwo:
# [1.0, 1.0, 1.0],
# [4.0, 8.0, 16.0],
# [9.0, 27.0, 81.0],
# [16.0, 64.0, 256.0],
# [25.0, 125.0, 625.0],
# Use math module to compute power of some number.

# List using list comprehensions vs type casting
listOne = [num for num in range(1, 6)]
# listOne = list(range(1,6))

# Create a listTwo that stores power of each num from listOne
listTwo = [ [pow(num, 1), pow(num, 2), pow(num, 3)] for num in listOne]

# Print result on screen
print("List Two:")

# Navigate to item list in listTwo
for item in listTwo:
    # print each element of item list
    for element in item:
        print(element, end=", ")

    print()

print()
print()


# ================================================
# Generate a multi-dimensional list of 10 by 10 elements.
# Also change [2][5] element to 20
# Sample output:
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
# [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
# [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
# [6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
# [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
# [8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
# [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]


# generate a list
listOfNums = [ [num] * 10 for num in range(10)]

# print listOfNums
for item in listOfNums:
    print(item)

print()
print()


# ===========================================
# Use two nested for loops to print all index and
# elements of the multi-dimensional list
# Use multi-dimensional list of 4 x 4
# Desired Output:
# [0][0] : 0 || [0][1] : 0 || [0][2] : 0 || [0][3] : 0
#
# [1][0] : 1 || [1][1] : 1 || [1][2] : 1 || [1][3] : 1
#
# [2][0] : 2 || [2][1] : 2 || [2][2] : 2 || [2][3] : 2
#
# [3][0] : 3 || [3][1] : 3 || [3][2] : 3 || [3][3] : 3



# Generating a list
listOfValues = [[i] * 4 for i in range(4)]

# Print each element of the list
for row in range(4):
    for col in range(4):
        print("[{}][{}] : {}".format(row,col, listOfValues[row][col]), end=" || ")

    # Remove " || " from end of line and add a new line.
    print("\b\b\b\b\n")


# ======================================================
# Generate a list of multiplication tables:
# Print tables from 2 to 10
# Use list comprehension and append function of list.
# Desired Output:
# 02, 04, 06, 08, 10, 12, 14, 16, 18, 20
# 03, 06, 09, 12, 15, 18, 21, 24, 27, 30
# 04, 08, 12, 16, 20, 24, 28, 32, 36, 40
# 05, 10, 15, 20, 25, 30, 35, 40, 45, 50
# 06, 12, 18, 24, 30, 36, 42, 48, 54, 60
# 07, 14, 21, 28, 35, 42, 49, 56, 63, 70
# 08, 16, 24, 32, 40, 48, 56, 64, 72, 80
# 09, 18, 27, 36, 45, 54, 63, 72, 81, 90



# Create a global variable to store tables
table = []

# Iterate for printing tables from 2 to 10
for tableNum in range(2, 10):
    # Use append function to add item to list.
    table.append([ tableNum * i for i in range(1, 11)])

# Print each table seperated by commas
for item in table:

    # Print a table
    for element in item:
        print("{:02}".format(element), end=", ")

    # Insert blank line after table
    print("\b\b\n")


