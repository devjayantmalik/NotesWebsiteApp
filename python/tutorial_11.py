# ==================================================
# ==================================================
#     Static, modules and exception handling
# ==================================================
# ==================================================


# ===========================================
# Static methods inside class
# Create a class with static method and use that
# static method without initialization in main()

class Sum:

    @staticmethod
    def get_sum(*args):
        # Creating a variable to store sum
        sum = 0

        # Using for loop to calculate sum
        for num in args:
            sum += num

        # return sum back from function
        return sum


def main():

    # Printing sum using get_sum() method
    print("Sum:", Sum.get_sum(1,2,3,4,5))


main()


# ===============================================
# Static variable inside class
# Create a class Dog and init method with name field
# Create a static variable inside dog class
# Every time the class is initialized the increment
# the static variable
# Create a static method inside dog class that,
# retrieves no of dogs initialized

class Dog:

    noOfDogs = 0

    def __init__(self, name):
        # Creating a field name
        self.name = name

        # incrementing static field
        Dog.noOfDogs += 1

    @staticmethod
    def get_no_of_dogs():
        print("There are currently {} dogs".format(Dog.noOfDogs))


def main():

    # Create 3 dog objects
    dog1 = Dog("Dog 1")
    dog2 = Dog("Dog 2")
    dog3 = Dog("Dog 3")

    # Calling static method to print no of dogs created
    Dog.get_no_of_dogs()
    dog1.get_no_of_dogs()
    dog2.get_no_of_dogs()
    dog3.get_no_of_dogs()


main()


# ========================================================
# Create a seperate file arithmetic.py
# Create 2 function sumAll and multiplyAll
# Use module import syntax to use those functions in main file

import tutorial_11_arithmetic as arithmetic

print("Sum using arithmetic:", arithmetic.sumAll(1, 2, 3, 4, 5))
print("Multiply using arithmetic:", arithmetic.multiplyAll(1, 2, 3, 4))


# ================================================
# Use from module_name import function_name
# use from module_name import *
# Use import module_name
# Use import module_name as variable

'''
# Import specific functions from tutorial_11_arithmetic
from tutorial_11_arithmetic import sumAll

print("Direct method invocation of sumAll:", sumAll(1, 2, 3, 4, 5))
'''

'''
# Import everything from module tutorial_11_arithmetic
from tutorial_11_arithmetic import *

print("in import * sum invocation:", sumAll(1,2,3,4,5))
'''

'''
# Import a module as arithmetic
import tutorial_11_arithmetic as arithmetic

print("Use of as:", arithmetic.sumAll(1,2,3,4,5))
'''

'''
# Import a module with all fields and methods
import tutorial_11_arithmetic
print("Use of single import:", tutorial_11_arithmetic.sumAll(1,2,3,4,5))
'''


# ==========================================
#       Exception Handling
# ==========================================

# Create a list of 5 elements and print
# element at 10th index in the list.
# also handle other exception if any occurs

try:
    aList = [1,2,3,4,5,6]

    # Try to print out of range index
    print(aList[10])

except IndexError:
    print("Index does not exist in the list.")

except:
    print("Unknown error occurred")


# =============================================
# Creating Custom exceptions
# Create a custom exception InvalidNumber
# Ask user to enter a no and accept the input as string
# If the string contains alphabets then
# raise InvalidNumber exception

# Rule:
# Use if statement + any() + list comprehension

class InvalidNumber(Exception):

    # Initializing a class
    def __init__(self, *args, **kwargs):
        Exception(self, *args, **kwargs)


try:
    num = input("Enter number: ")

    if any( char.isalpha() for char in num):
        raise InvalidNumber

except InvalidNumber:
    print("Number cannot contains alphabets")


# ===============================================
# Write a program to get two numbers for division: num1, num2
# try to divide the no and get the quotient
# if success then print the result
# handle divide by zero exception
# Also use else and finally keywords outside of try block


# Ask user for 2 nums
num1, num2 = input("Enter two nums: ").split()

# Try to divide the nos
try:
    quotient = int(num1) / int(num2)

    print("{} / {} = {}".format(num1, num2, quotient))

# catch zero division error
except ZeroDivisionError:
    print("You cannot divide by zero.")

# Use of else if no exception occurs
else:
    print("No exception raised.")

# use of finally to execute code irrespective of exception occurence
finally:
    print("I don't care about exception.")


# ===============================================
# 1. Create a file named info.txt
# 2. Open the file without using with keyword (open in try)
# 3. Catch FileNotFoundError and prints exception args using as keyword
# 4. In else print contents of file
# 5. In finally print Thanks for using our software
# 6. Open non existent file activation.txt

try:
   file = open("/home/hp/temp/info.txt", mode="r", encoding="utf-8")

   # Tried at last to raise and catch exception FileNotFoundError
   # file2 = open("/home/hp/temp/info.txt", mode="r")

except FileNotFoundError:
    print("File not found on disk.")

else:
    # print contents of the file
    for word in file.readlines():
        print(word, end="")

    # close the file
    file.close()

finally:
    print("Thanks for using our software.")


