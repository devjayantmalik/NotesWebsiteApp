# ==================================================
# ==================================================
#   Functions as objects, function Annotations,
#   Lambda Anonymous functions, Map, filter,
#   Reduce
# ==================================================
# ==================================================

# Create a function to return num * 2
# Assign the function to a variable
# Now use that variable for function invocation

def multiply_by_two(num):
    return int(num) * 2

times2 = multiply_by_two

print("4 * 2 =", times2(4))

# =============================================
# Use the above function multiply_by_two as it is
# Create a function math_is_fun() and receive function2 and num1 as its argument
# Now return function2(num1)

def math_is_fun(func, num):
    return func(num)

print("Math is fun: 4 * 2 =", math_is_fun(times2, 4))



# ===============================================
# Return a function from within a function
# and also demonstrate dynamically create a function

# Hints:
# Create a function with argument one
# Create another function2 in body of function1 with argument two
# return function2
# Store the output in generated_function

def multiply_by_custom(num):

    def multiply(value):
        return num * value

    return multiply


# create two variable
num1 = 10
num2 = 20

# Receiving function
generated_func = multiply_by_custom(num1)

# Using generated function.
print("{} x {} = {}".format(num1, num2, generated_func(num2)))


# =======================================
# Store functions inside of data structures : generated_func, multiply_by_two
# Now access the functions using index


# Creating a list of functions
list_of_funcs = [multiply_by_two, generated_func]

# Accessing function from list
print("10 x 7 =", list_of_funcs[1](7))


# =================================================
# Create a function that receives a list and a function
# The function passed will return True or False if a list value is odd
# The surrounding function will return a list of odd numbers.

def get_odd_status(num):
    if num % 2 != 0:
        return True
    else:
        return False


def do_something_crazy(func, nums):
    data = []

    for i in nums:
        if func(i):
            data.append(i)

    return data


def main():

    # Creating a list to pass to function
    elements = [1, 2, 3, 4, 5, 6, 7, 8]

    # Calling do_something_crazy() function
    result = do_something_crazy(get_odd_status, elements)

    # Print result
    for num in result:
        print(num, end=", ")

    print("\b\b\n")

main()




# ==============================================
#           Function Annotations
# =============================================

# Function annotations are used for documentation purposed only.
# These have no impact on behaviour of function


# ================================================
# Create a function world_is_awesome with
# name as string, age as int datatype specified in function
# Also use the function annotation to specify that the function
# returns string
# Demonstrate how to print the annotations of the function

def world_is_awesome(name: str, age: int) -> str:
    return "{} is {} years old".format(name, age)


result1 = world_is_awesome("Jayant", 10)

result2 = world_is_awesome("Mohit", "20")

print(result1)
print(result2)

print(world_is_awesome.__annotations__)


# ==========================================
#           Lambda Functions
# ==========================================

# Lambda functions do not require a name and they are
# also known as anonymous function.

# Syntax:
# lambda arg1, arg2, arg3, arg4:
#       expression or statements


# ======================================
# Create a lambda function to add 3 nums

sum = lambda x, y, z : x + y + z

print("Sum:", sum(1,2,3))


# ======================================
# Create a lambda function to return true
# if a person can vote and false if he can't
# Use ternary operator to solve this problem

canVote = lambda age: True if age >= 18 else False

print("Can a person with 19 years age vote? :", canVote(19) )
print("Can a person with 12 years age vote? :", canVote(12) )


# =============================================
# Create a list of lambda functions to calculate
# different power of numbers taking num as argument.
# Let's say we pass num = 4
# Then we should be able to calculate 4 ** 2, 4 ** 3, 4 ** 4
# Use for loop to execute each function

powersList = [lambda x: x **2,
              lambda x: x **3,
              lambda x: x **4]

num = 4

# Using for loop to execute functions
for func in powersList:
    print(func(num))

# =============================================
# Store lambdas inside of dictionary
# Use warrior attack as an example
# Create three keys inside of dictionary: quick, power, miss
# and Quick Attack, Power Attack, Missed Attack using lambda function

# Use random module to generate random choice from a list of items
# Use list() type cast to convert a dictionary to list


# Create a dictionary to store lambdas
warriorsAttack = {'quick': (lambda : print("Quick Attack")),
                  'power': (lambda : print("Power Attack")),
                  'miss': (lambda : print("Missed Attack"))
                  }

# Import random module to generate random choice
import random

# Get a choice from the list of keys
choice = random.choice(list(warriorsAttack.keys()))

# Calling the lambda function
warriorsAttack[choice]()


# ===============================================
# Create a random list filled with the characters 'H' or 'T'
# for heads and tails
# Output the no of heads and tails
# Ask the user no of times the coin was tossed

# Sample output:
# Enter no of times the coin was tossed: 50
# Heads: 46
# Tails: 54


# Import the random module
import random

# Ask the user for no of times the coin was tossed
# times = int(input("Enter no of times the coin was tossed: "))
times = 100
# Create variables to store heads and tails
heads = 0
tails = 0

# Create a lambda function to get heads or tails
get_random_tails = lambda : random.choice(['H', 'T'])


# Iterate times
for _ in range(times):
    # Get the random tails
    result = get_random_tails()

    # increment the tails if
    if result == 'H':
        heads += 1
    else:
        tails += 1


# Print heads and tails
print("Heads:", heads)
print("Tails:", tails)



# =============================================
#               Map
# =============================================

# Map allows us to operate a function on all items of the list.

# ===============================================
# Generate a list of numbers from 1 to 10
# Create a function that returns num * 2
# Use map function to print doubles of the each no in the list


# Creating a list
oneTo10 = range(1, 11)

# Create a function
def double_x(num):
    return num * 2

# Using map function to generate a list of double of each item
items = list(map(double_x, oneTo10))

print("Items using function + map", items)


# ==================================
# Use lambda and map to get doubles of above list oneTo10


# Generating list of values and assign them to items
items = list(map(lambda x: x * 2, oneTo10))

# Print the result on the screen
print("Items using lambda + map:", items)


# ============================================
# Create two lists and use lambda to add
# same element at index of list1 to element at
# same index in list2

# Creating 2 lists
list1 = list(range(1, 5))
list2 = list(range(5, 10))

# Generating list of values
vals = list(map((lambda x, y: x + y), list1, list2))

# Print lists
print(list1)
print(list2)
print(vals)


# =========================================
# print 3 blank lines using single print statement
print("\n" * 3)


# ==========================================
#           Filter
# ==========================================


# ===========================================
# Use filter and lambda to generate even values from the list
# Use range function to generate a list

# Creating a list of values
data = list(range(1, 11))

# Using filter and lambda to generate even nos
evens = list(filter((lambda x: x % 2 == 0), data))

# Print evens on screen
print(evens)


# ===================================================
# Find the multiples of 9 from a random 100 value list with
# values between 1 and 1000

# Import random module to generate a list
import random

# Generated a list
list_of_vals = [ random.randint(1, 1000) for _ in range(100)]

# Using filter and lambda to check for multiples of 9
multiples = list(filter((lambda x: x % 9 == 0), list_of_vals))

# Print multiples on screen
print(multiples)


# =============================================
#                   Reduce
# =============================================

# To use reduce import it from functools module
# Reduce receives a list and returns a single result


# =============================================
# Add all the values in the list using reduce
# use range function to generate a list
# Use lambda to sum two nos

# import reduce
from functools import reduce

# Calculate the sum
sum = reduce((lambda x, y: x + y), range(1, 6))

# Print sum
print("Sum using reduce:", sum)


