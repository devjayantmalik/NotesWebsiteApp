# ==================================================
# ==================================================
#               Python Threads
# ==================================================
# ==================================================

# Threads: A block of code that executes by taking turns,
# for example: lets say first threads executes then
# it sleeps and second thread executes
# threads are concepts of parallel processing

# Threading module is used to create threads in python
# Reference: https://pymotw.com/2/threading/


# ==========================================
# Create a function that calculates sum of n nums and then prints it
# Use threading module to run the function as seperate thread
# Also print current thread in sum function and in main function
# Hint: Use join function to schedule thread along with main thread
import threading

def calculate_sum(*args):
    sum = 0
    for num in args:
        sum += num

    print("Sum:", sum)
    print("Current Thread:", threading.current_thread())


# Created a thread
task = threading.Thread(target=calculate_sum, args=(range(1, 10000)))

# Call for thread to run
task.start()

# Call for join function to schedule task along with main thread
task.join()

# Check for active threads
print("Current Thread:", threading.current_thread())


# ===============================================
# Create a function and implement it as follows:
# 1. Function should take one argument: thread_no
# 2. Print "Thread {thread_no} sleeps at {formatted_time}"
# 3. Generate a random no for sleep seconds
# 4. Call the sleep function in time module to sleep the thread
# 5. Print "Thread {thread_no} wakes at {formatted_time}"
# Now, use a for loop to create 10 threads
# Implement the for loop such that:
# 1. Create a thread object
# 2. Execute or start the thread object
# 3. Print the currently active threads count
# 4. Print the list of all active threads
# Use threading, time, and random module in the example


import threading
import time
import random


def execute_thread(thread_no):
    # Printing initial thread time
    print("Thread {} sleeps at {}".format(
        thread_no,
        time.strftime("%H:%M:%S", time.gmtime())
    ))

    # Generate a random sleep time
    randSleepTime = random.randrange(1, 5)

    # Make the thread sleep
    time.sleep(randSleepTime)

    # Print thread awekening time from sleep
    print("Thread {} stops sleeping at {}".format(
        thread_no, time.strftime("%H:%M:%S", time.gmtime())
    ))


# Creating 10 threads and running them
for i in range(10):
    # Creating a thread
    thread = threading.Thread(target=execute_thread, args=(i,))

    # Start the thread
    thread.start()

    # Print active threads
    print("Active Threads:", threading.activeCount())

    # Getting a list of active thread objects
    print("Thread Objects:", threading.enumerate())


# ===========================================
#       Sub Class a thread
# ===========================================
# Create a getTime function that:
# Takes thread_name as input
# Prints "Thread {name} sleeps at {time}"
# generate a random sleep time
# sleeps the thread

# Create a Class CustomThread() and take name as input to the class
# In the CustomThread:
# inititalize the thread and threading.Thread class
# create a class field name
# define the run method and call getTime() inside of the class


# Import statements
import time
import threading
import random


def getTime(name):
    # Prints sleeping time of thread
    print("Thread {} sleeps at {}".format(
        name,
        time.strftime("%H:%M:%S", time.gmtime())))

    # Generate random seconds between 1 and 5
    sleepTime = random.randint(1, 5)

    # Call for sleep
    time.sleep(sleepTime)

    # Prints waking time of thread
    print("Thread {} wakes at {}".format(
        name,
        time.strftime("%H:%M:%S", time.gmtime())
    ))


class CustomThread(threading.Thread):

    # Initialize method implementation
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    # Defining run method to execute thread
    def run(self):
        getTime(self.name)


# Creating 2 threads
thread1 = CustomThread("1")
thread2 = CustomThread("2")

# Start execution of threads
thread1.start()
thread2.start()

# Check if threads are alive
print("Is Thread 1 alive:", thread1.is_alive())
print("Is Thread 2 alive:", thread2.is_alive())

# Get thread name
print("Thread 1 Name:", thread1.getName())
print("Thread 2 Name:", thread2.getName())

# Change thread names
thread1.setName('First Thread')
thread2.setName('Second Thread')

# Join allows us to wait for threads to execute
thread1.join()
thread2.join()

print("Execution Ends")


# ==========================================
#       Locking Threads
# ==========================================
# Locking of threads in real world:
# let's say we want to model a bank account transaction
# If there are 3 persons logged in same bank account at same time
# then we do want transaction from user1 to complete and after that
# complete transaction of user2 then complete transaction of user3

# Why we did that?
# Let's say we have 100 rs in our bank account
# All users did the transaction at same time from
# same account(one from atm, online banking, debit card)
# first user: asked to transact 90 rs
# second user: asked to transact 100 rs
# third user asked to transact 50 rs

# The process:
# Thread 1 will transact 90 rs and sleep (incomplete transaction)
# then thread 2 will transact 100 rs and sleep(incomplete transaction)
# again thread 1 will complete execution
# thread 2 will complete execution

# so, if 2 threads were running then we payed 190 rs whereas
# the person had only 100 rs in bank balance


# ==========================================
'''
Create a class Bank Account
Initialize the class with 2 args: name, moneyRequest
inside of run():
1. lock the thread
2. Call getMoney method in Bank Account
    Class (implement as static method) with self as argument
3. Release the lock from thread

Implementing getMoney() method:
1. Print "{customer.name} tried to withdraw {moneyRequest} at {current_time}"
2. Check if customer has enough account balance
3. if true: then deduct account balance and print "new account balance"
4. else print "Insufficient balance" and "current balance"

Implementing main function:
1. Create 3 customers with withdraw amount as (1, full_balance, half_of_balance)
2. Start threads for all customers
3. Call join on all 3 threads
4. print "execution ends"
'''



import threading
import time

class BankAccount(threading.Thread):

    bankBalance = 100

    def __init__(self, name, withdrawAmount):
        threading.Thread.__init__(self)

        self.name = name
        self.withdrawAmount = withdrawAmount

    def run(self):
        # Lock the thread
        lock.acquire()

        # Make transaction
        self.withdraw(self)

        # Release the lock
        lock.release()

    @staticmethod
    def withdraw(customer):
        # print info related to transaction
        print("{} tries to withdraw {} at {}".format(
            customer.name, customer.withdrawAmount,
            time.strftime("%H:%M:%S", time.gmtime())
        ))

        # Check for acc balance
        if BankAccount.bankBalance - customer.withdrawAmount > 0:
            # Deduct the balance
            BankAccount.bankBalance -= customer.withdrawAmount

            # Print new balance
            print("Transaction Successful.")
            print("New Account Balance:", BankAccount.bankBalance)

        else:
            print("Insufficient Account Balance")

        time.sleep(3)

# Creating a lock
lock = threading.Lock()

# Creating 3 customers
jayant = BankAccount('Jayant Malik', 1)
shaurya = BankAccount('Shaurya', 100)
mohit = BankAccount('Mohit', 50)

# Start the threads
jayant.start()
shaurya.start()
mohit.start()

# Join the threads in active threads list
jayant.join()
shaurya.join()
mohit.join()

# Print for the transaction ends
print("Transaction Ends")