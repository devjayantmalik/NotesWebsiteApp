# ==================================================
# ==================================================
#               Object Oriented programming
# ==================================================
# ==================================================

# What are:
# Objects, Fields, Methods, Class

# ==========================================
# Model an object human using object oriented programming
# Create a class
# Create a init method and explain self keyword
# Create methods and fields about a human

# Now we have above template setup
# Create 3 human named jayant, sahil, vikas

class Human:

    # Receiving name, age, height and weight when class is initialized.
    def __init__(self, name="", age=0, height=0, weight=0):

        # Defining fields and assigning them values
        # passed to class when initialized
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    # Defining methods
    def walk(self):
        print("{} is the human that walks...".format(self.name))

    def speak(self):
        print("{} is the human that speaks...".format(self.name))

    def introduce(self):
        print("{} is my name and i am {} years old. "
              "My height is {} foot and weight is {} kg."
              .format(self.name, self.age, self.height, self.weight))

    def bark(self):
        print("{} cannot bark, because he is a human...".format(self.name))


# Defining main function
def main():

    # Creating a human object
    jayant = Human('Jayant Malik', 18, 5, 50)

    # Calling methods of jayant object
    jayant.speak()
    jayant.bark()
    jayant.introduce()
    jayant.walk()


    return 0

# Invoking main function
main()


# ===========================================
# Getters and Setters
# Create a class Rectangle
# Create two fields: height and width
# Use of keywords :
# @property
# @variable_name.setter
# __variableName
#



# Creating a class square
class Rectangle:

    # Defining init method that will be called during initialization
    def __init__(self, height=0, width=0):
        self.height = height
        self.width = width


    # Using @property keyword for getter
    @property
    def height(self):
        print("Retrieving height of square...")

        return self.__height

    # Using @variable_name.setter keyword for setter
    @height.setter
    def height(self, value):

        # Check for valid value
        if str(value).isdigit():
            self.__height = value

        else:
            print("Invalid value provided")

    # Using @property keyword for getter
    @property
    def width(self):
        print("Retrieving width of square...")

        return self.__width

    # Using @variable_name.setter keyword for setter
    @width.setter
    def width(self, value):

        # Check for valid value
        if str(value).isdigit():
            self.__width = value

        else:
            print("Invalid value provided")


    # Implementing methods related to rectangle
    def get_area(self):

        return self.__height * self.__width





def main():

    # Creating an object sqr
    sqr = Rectangle()

    # Setting value of width
    sqr.width = 10
    sqr.height = 5

    # Accessing value of height from square
    print(sqr.height)
    print(sqr.width)

    return 0


main()



# ======================================================================
# Create a warrior game where two warriors fight till one dies

# Help and Hints:
# Warriors Class:
# Warriors will have names, health, and attack and block maximums
# Warriors will have capibilities to attack and block random amounts

# attack method: random() * maxAttack
# block method: random() * minAttack

# Battle Class:
# Will have capibality of looping till one warrior dies.
# Warriors will each get a turn to attack each other

# Function gets 2 warriors:
# one warrior will attack the other

# Attacks and blocks should be integers


# Sample output:
'''
Tom attacked Paul and deals 1 damange
Paul is down to 9 health
Paul attacked Tom and deals 2 damange
Tom is down to 9 health
Tom attacked Paul and deals 5 damange
Paul is down to 5 health
Paul attacked Tom and deals 6 damange
Tom is down to 5 health
Tom attacked Paul and deals 8 damange
Paul is down to 2 health
Paul attacked Tom and deals 5 damange
Tom is down to 2 health
Tom attacked Paul and deals 10 damange
Paul is down to 0 health
Game Over
'''

# Import random module to generate random no
import random

# Create a warrior class
class Warrior:

    # Initializing the class
    def __init__(self, name="", health=0, maxAttack=50, maxBlock=10):
        self.__name = name
        self.__health = health
        self.__maxAttack = maxAttack
        self.__maxBlock = maxBlock

    # Setting getters
    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @property
    def maxAttack(self):
        return self.__maxAttack

    @property
    def maxBlock(self):
        return self.__maxBlock

    # Setting setters
    @name.setter
    def name(self, name):
        self.__name = name

    @health.setter
    def health(self, health):
        if str(health).isdigit():
            self.__health = health
        else:
            print("Invalid health")

    @maxAttack.setter
    def maxAttack(self, attack):
        if str(attack).isdigit():
            self.__maxAttack = attack
        else:
            print("Invalid attack value")

    @maxBlock.setter
    def maxBlock(self, block):
        if str(block).isdigit():
            self.__maxBlock = block
        else:
            print("Invalid block value")


    # Defining methods

    def attack_warrior(self, maxAttack):
        return int(abs(random.random() * maxAttack))

    def block_warrior(self, maxBlock):
        return int(abs(random.random() * maxBlock))


# Creating Battle class
class Battle:

    # Initializing the class
    def __init__(self, warrior1, warrior2):
        self.warrior1 = warrior1
        self.warrior2 = warrior2

    # Creating methods
    def start_fight(self):
        health1 = self.warrior1.health
        health2 = self.warrior2.health

        while health1 > 0 and health2 > 0:
            # Attack warrior and change health as per the the result
            health2 -= self.get_attack_result(self.warrior1, self.warrior2)

            # check if health is negative
            if health2 < 0: health2 = 0

            # print the result on the screen
            print("{} attacked {} and deals {} damange".format(self.warrior1.name, self.warrior2.name, self.warrior2.health - health2))
            print("{} is down to {} health".format(self.warrior2.name, health2))

            if health2 == 0:
                print("Game Over")
                break

            # change the health and print the result
            health1 -= self.get_attack_result(self.warrior2, self.warrior1)

            # check if health is negative
            if health1 < 0: health1 = 0

            print("{} attacked {} and deals {} damange".format(self.warrior2.name, self.warrior1.name, self.warrior1.health - health1))
            print("{} is down to {} health".format(self.warrior1.name, health2))

            if health1 == 0:
                print("Game Over")

    def get_attack_result(self, warrior1, warrior2):

            # Get attack value of warrior1 and block value of warrior2
            attack = warrior1.attack_warrior(self.warrior1.maxAttack)
            block = warrior2.block_warrior(self.warrior2.maxBlock)

            # return damage of warrior 2
            return attack - block



def main():
    # Create two warriors
    tom = Warrior("Tom", 10, 5, 2)
    paul = Warrior("Paul", 10, 5, 2)

    # Initialize the battle
    fight = Battle(tom, paul)

    # Start the fight
    fight.start_fight()

if __name__ == '__main__':
    main()



