# ==================================================
# ==================================================
#    Dictionaries and Recursive functions
# ==================================================
# ==================================================




# Create a dictionary
# Perform the below operations using [] syntax:
    # Access value of the dictionary using key
    # Change value of dictionary element using key
    # Show that dictionary are non sequential
    # Add a element in dictionary

# Check if a key exists in dictionary using 'in statement'
# Retrieve a list of values from dictionary
# Retrieve a list of keys from dictionary
# Retrieve a list of items seperated in form of tuple from dictionary
# Use a for loop and items() method to get a list of elements from dictionary
# Get an element from the dictionary using get() method and
# if the element does not exist then print default value
# Delete a key value from dictionary using del statement
# Delete all elements of the dictionary
# Create an empty list and append a dictionary to the list


# Creating a dictionary
record = {'fName': 'Jayant', 'lName': 'Malik', 'address': 'Mohkra', 'college': 'vaish'}

# Accessing element of the dictionary using key
print("Name in record:", record['fName'])

# Changing element in dictionary
record['fName'] = 'Mohit'

# Elements in the dictionary are non - sequential
print("Dictionary printed as it is:", record)

# Add another element to the record and print it
record['phone'] = '125245585'
print("Phone added in dictionary:", record)

# Check if an element exists in dictionary
print("Does phone exist in record:", "phone" in record)

# Retrieve a list of values from dictionary
print("List of values from dictionary:", record.items())

# Retrieve a list of keys from dictionary
print("List of keys from dictionary:", record.keys())

# Retrieve a list of items seperated in form of tuple from dictionary
# print("List of items in form of tuple:", record.items())

# Use a for loop and items() method to get a list of elements from dictionary
for key, value in record.items():
    print(key, value)

# Get an element from the dictionary using get() method and
# if the element does not exist then print default value
print("fName from record:", record.get('fName', "key not found"))

# Delete a key value from dictionary using del statement
del record['phone']

# Delete all elements of the dictionary
record.clear()


# ===========================================================
# Ask user to enter first name and last name seperated by spaces
# Then create an empty list
# Then Append the fName and lName to the list in form of dictionary
# Now print the list

# Sample Output:
# Enter your name: Jayant Malik
# list with dictionary item: [{'fName': 'Jayant', 'lName': 'Malik'}]

# Declare variables
fName, lName = "", ""

# Ask user for name
try:
    fName, lName = input("Enter your name: ").split()
except ValueError:
    print("Invalid Input")
    exit(0)

# create en empty list
data = []

# Now append the item to the list
data.append({"fName": fName, "lName": lName})

# Print the list
print("list with dictionary item:", data)


# ================================================
# Write a program that generates this sample output.
# Enter Customer (Yes, No) : y
# Enter Customer Name : Jayant Malik
# Enter Customer (Yes, No) : y
# Enter Customer Name : Mohit Sharma
# Enter Customer (Yes, No) : n
# Customers added are:
# Jayant Malik
# Mohit Sharma

# Create a list to hold dictionary values
customers = []

# Create variable for first name and last name
fName = ''
lName = ''

while True:
    try:
        # Ask user for customer enter choice
        status = input("Enter Customer (Yes, No) : ")

        # if user enters status as y or yes then prompt for name
        if status.lower() == 'y' or status.lower() == 'yes':
            try:

                # Ask user for name
                fName, lName = input("Enter Customer Name: ").split()

                # Store the name in list as a dictionary
                customers.append({'fName': fName, 'lName': lName})

            except ValueError:
                print("Invalid Input ")
                exit(0)

        # else exit
        else:
            break

    except ValueError:
        continue


# Print the customer names on the screen
for customer in customers:
    print(customer.get('fName', "Key not found error"),
          customer.get('lName', "Key not found error"))


# =======================================================
#           Recursive functions
# =======================================================


# Write a program to compute factorial of a number
# Ask user for input
# Use recursive function to solve the problem
# Use exception handling to check for invalid no passed inside factorial function
# If invalid input is provided print invalid input and exit the program

def calculate_factorial(num):
    try:
        # convert num to int
        num = int(num)

        # if num <= 1: return 1
        if num <= 1:
            return 1

        # else return num * factorial(num - 1)
        else:
            return num * calculate_factorial(num -1)

    except:
        print("Invalid Input supplied")
        exit(0)


# Ask user for number
number = input("Enter a number: ")

# Calculate factorial and print it
print("Factorial of", number, "is", calculate_factorial(number))


# =========================================================
# Write a program to calulate fibonachi series using recursive functions
# Conditions for fibonacchi:
# If no is 0 then return 0
# if no is 1 then reurn 0
# if not is neither 0 nor 1 then return fib(no - 1) + fib(no - 2)

# Sample output for 20 fibs:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181


def calculate_fib(number):
    if number == 0:
        return 0

    elif number == 1:
        return 1

    else:
        return calculate_fib(number - 1) + calculate_fib(number - 2)



for i in range(20):
    print(calculate_fib(i), end=", ")

print("\b\b\n")

