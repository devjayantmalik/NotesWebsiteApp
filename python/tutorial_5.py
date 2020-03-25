# ==================================================
# ==================================================
#               Functions
# ==================================================
# ==================================================


# ===============================================
# Write a function to add two numbers

def add_numbers(num1, num2):
    return num1 + num2

sum = add_numbers(5, 3)
print("5 + 3 =", sum)


# ===============================================
# Example to demonstrate that variable created
# inside function is available only inside function

def assign_name():
    name = "Vikash"
    print("name inside function:", name)

# create a global variable
name = "Jayant Malik"

# Use assign name to change the variable
assign_name()

# print the name
print("name outside function:", name)


# ========================================================
# Create a global variable 'name'
# create a function change_name(name) and
# assign name="Tom" inside function
# pass the global variable inside change_name()
# print value of name outside the function

# Defining a function change_name()
def change_name(name):
    name = "Tom"

# Creating a global variable
name = "Jayant Malik"

# Call the change_name() function
change_name(name)

# Print the value of name
print("Value of name is:", name)


# ==========================================================
# Change value of global variable by
# returning some value from function

# Define a function
def change_name(name):
    return name

# Create a global variable 'name'
name = "Jayant Malik"

# Print initial value of name
print("Initial Name:", name)

# Call change_name() function and assign value to name
name = change_name("Donald Trump")

# Print name on the screen
print("Changed Name:", name)


# ===========================================================
# Change the global variable using global keyword

# Create a function change_name()
def change_name():
    global global_name
    global_name = "Peter"

# Declare a global variable and print its initial value
global_name = "Arvind"
print("Using global initial name:", global_name)

# Call change_name function
change_name()

# Print changed value of global_name
print("using global changed name:", global_name)


# =================================================
# Example to demonstrate that a function
# without a return value returns None


# Declare a function
def say_hello():
    print("Hello inside say_hello()")

result = say_hello()
print("Result from say_hello():", result)


# ====================================================
# Write a program to solve for x
# Sample output:
# Enter Equation: x + 4 = 9
# Result: x = 5

# Rules:
# First input will always be x and
# we need to only perform addition
# function will receive a single string and then split it into parts

# Create a function to solve for x
def solve_x(eqn):
    # Intial equation: x + val1 = val2
    # For soln Equation becomes: x = val2 - val1

    # Split the string into words
    x, plus, val1, equals, val2 = eqn.split(" ")

    # Solve for x
    return int(val2) - int(val1)

# Ask the user for equation and split it into parts
eqn = input("Enter Equation: ")

# Call the solve_x function and store the result
soln = solve_x(eqn)

# Print value of x
print("Result: x =", soln)


# ==================================================
# Create a function that returns multiple values at same time
# Also receive and store the values in result1, result2 variables
# Tips:
# Create a program to return addition and subtraction
# of two numbers at the same time.


# Declaring a multi_vals function with two arguments.
def multi_vals(num1, num2):
    return (num1 + num2), (num1 - num2)

# Receiving result from multi_vals function
addition, subtraction = multi_vals(5, 4)

# Print the results on screen
print("addition 5 + 4:", addition)
print("subtraction 5 - 4:", subtraction)


# ================================================
# Write a function that returns list of prime numbers
# A prime number is only divisible by 1 and itself
# 5 is a prime, because it is divisible only by 1 and 5
# 6 is not a prime, because it is divisible by 1, 2, 3, 6

# Rules:
# Create a seperate function to check if a no is prime
# Create a seperate function to return a list of prime nos


# Creating a function to check if a no is prime
def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False

    return True

# Creating a function to get a list of prime nos
def get_primes(upto):

    # list of prime nos
    listPrimes = [1]

    # a loop to generate no from 1 to upto
    for i in range(2, upto):
        if is_prime(i) == True:
            listPrimes.append(i)

    # return listPrimes back
    return listPrimes


# Ask the user for max no upto which he wants a list to be generated
upto = int(input("Enter upto: "))

# Receive list of primes and store it in a variable
primes = get_primes(upto)

# print primes on screen
for prime in primes:
    print(prime, end=", ")

print("\b\b")


# =======================================================
# Create a function to receive unknown no of arguments
# Use splat operator (*)

# Create a function to sum n numbers
def sum_all(*args):
    # Create a variable to store sum
    sum = 0

    # cycling through each argument passed
    for num in args:
        sum += num

    # Return the final sum
    return sum

# Assigning sum to variable
result = sum_all(1,2,3,4,5,6)

# Print the sum on the screen
print("Result:", result)


# ==============================================
# Write a program to calculate area of different shapes:
# Ignore case in which input is provided by user.

# Sample output:
# Enter shape: rectangle
# Area of Rectange is :

# Import math module
import math

def rectangle_area():
    # Ask the user for length and breadth
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))

    # Calculate the area
    area = length * breadth

    # Print the area on screen
    print("Area of rectangle: {} x {} = {}".format(length, breadth, area))

def square_area():
    # Ask for side
    side = float(input("Enter side: "))

    # Calculate the area
    area = math.pow(side, 2)

    # Print the area on screen
    print("Area of square: {} x {} = {}".format(side, side, area))


def circle_area():
    # Ask for radius
    radius = int(input("Enter radius: "))

    # Calculate the area
    area = math.pi * math.pow(radius, 2)

    # Print the result on screen
    print("Area of circle: {:.6f} x {} x {}".format(math.pi, radius, radius))


def get_area(shape):
    # Convert shape to lower case
    shape = shape.lower()

    # Check for shapes
    if shape == "rectangle":
        rectangle_area()
    elif shape == "square":
        square_area()
    elif shape == "circle":
        circle_area()
    else:
        print("Invalid shape entered.")


def main():
    # Ask the user for type of shape
    shape = input("Enter shape (rectangle, square, circle): ")

    # Call get_area() function
    get_area(shape)

main()


