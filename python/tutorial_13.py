# ==================================================
# ==================================================
#    Iterabale, Iterator, List Comprehensions,
#   Generator Functions, Generator Expressions
# ==================================================
# ==================================================


# Difference between Iterator and Iterable:
# Iterable:
# It is a series of elements that can be iterated.
# It does not have any iteration state such as, "current element",
# instead it has one method that produces an iterator.
# The object is named __iter__

# Iterator:
# It is an object with iteration state.
# It lets you check if it has more
# elements using hasNext()(in case of java) method
# and move to next element using next() method
# The object is named __next__

# =================================
# Example to demonstrate iterator
# Create a string and convert it into iterator
# Now, Use next method to print character of string

name = iter("Jayant Malik")

print(next(name))
print(next(name))
print(next(name))


# ====================================
# Create an Alphabet class and implement it as iterable

class Alphabet:

    def __init__(self):
        self.letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.index = -1

    # Making the class iterable
    def __iter__(self):
        return self

    # implementing next method in an iterator object
    def __next__(self):
        if self.index >= len(self.letters) - 1:
            raise StopIteration

        # Increment index and return character from string
        self.index += 1
        return self.letters[self.index]


def main():
    # Creating an alphabet object instance
    alphas = Alphabet()

    # Printing next character in alphabet
    print("Char: ", next(alphas))
    print("Char using Class:", next(Alphabet()))

    # Using for loop on alphas variable
    for character in alphas:
        print(character)

    # Using for loop on class object
    for character in Alphabet():
        print(character)

main()



# ======================================
# Example to show that dictionary is an iterable
# Create a dictionary and iterate through its values


# Creating a dictionary
record = {"fName": "Jayant", "lName": "Malik", "rollNo": "123"}

# Using for loop on record
for key in record:
    print(key, record[key])


# ===================================
# Create a class that returns values from fibonacci
# sequence each time next is called
# Sample output:
# Fib : 1
# Fib : 2
# Fib : 3
# Fib : 5

class Fibonacci:

    def __init__(self):
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        fibNum = self.first + self.second
        self.first, self.second = self.second, fibNum

        return fibNum


def main():
    fibs = Fibonacci()

    for fib in fibs:
        if fib > 1000:
            break

        print("Fib :", fib)

main()


# =======================================
#           List Comprehension
# =======================================

# Multiply every value in the range(1, 11) using map and
# then using list comprehension
# Use filter to print odd nos from 1 to 10 and do
# the same using list comprehension

# Using map
result = list(map((lambda num : num * 2), range(1, 11)))
print("Output using map:", result)

# Using list comprehension
print("Output using list comprehension:", [x * 2 for x in range(1, 11)])

# === Printing odds ====

# Using filter
print("Using Filter:", list(filter((lambda x: x % 2 != 0), range(1, 11))))

# Using list comprehension for odd nos
print("Using list c..:", [num for num in range(1, 11) if num % 2 != 0])


# ==============================
# Generate 50 values
# Take each value to power of 2
# Return multiples of 8
# Solve the above program using 2 approaches
# 1. Use list comprehension and filter only in single line
# 2. Use list comprehension, filter and map in single line

# Using just filter and list comprehension
result = list(filter( (lambda x: x % 8 == 0), [pow(2, x) for x in range(1, 51)]))
print(result)

# Using map filter and list comprehension
result = list(filter( (lambda x: x % 8 == 0) ,map( (lambda x: pow(2, x)), [x for x in range(1, 50)])))
print(result)


# ==================================================
# Generate a list of 50 random values between 1 and 1000
# and return those that are multiples of 9
# You will have to use list comprehension inside
# of list comprehension to solve the above challenge
# Use max of 2 lines to solve this problem

import random

result = [val for val in [random.randrange(1, 1001) for _ in range(50)] if val % 9 == 0]
print(result)


# ===================================================
# Create a multi dimensional list and
# print first column of the list using list comprehension
# Print diagnol elements using list comprehension

table = [
    [1, 2, 3],
    [2, 3, 4],
    [5, 6, 7]
]

# Printing first column
print("Col 1:", [row[1] for row in table])

# Printing diagnol elements
print("Diagnol Elements:", [table[i][i] for i in range(len(table))])

# ===================================================
#           Generator Functions
# ===================================================

# What is a generator?
# Genrerator is a function and a statement used,
# In order to prevent all values to be generated at once
# range() function uses generator

# Why do we use generators?
# Generators are used to in case of large data sets.
# Because large data sets will use more memory and thus
# slows down our os and program.
# A generator prevents all values to genrated at once, so
# we will get the value as we use it.


# ==========================================
# Create a generator to get a list of prime numbers
# Use yield keyword
# Note: If you use next() function after StopIteration,
# it will throw an error

# Function to check if a no is prime
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False

    return True

# Function to generate primes
def gen_primes(max_no):
    for i in range(1, max_no):
        if is_prime(i):
            yield i


# You can use gen_primes() without setting
# a reference, direct in loop
# Creating a reference to gen_primes()
prime = gen_primes(50)

# Using next to gen_prime
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))


# Using for loop to print primes
for num in prime:
    print(num, end=", ")

print("\b\b")

# ============================================
#       Generator Expressions
# ============================================

# Generator expressions use parenthesis '()' in syntax

# =========================================
# Create a generator expression to generate doubles
# of num from 1 to 15
# Use next function to get next double

# Writing a generator expression
double = (num * 2 for num in range(1, 16))

# Printing element using next
print("Double: ", next(double))
print("Double: ", next(double))

# Using for loop to print doubles
for num in double:
    print(num, end=", ")

print("\b\b")





