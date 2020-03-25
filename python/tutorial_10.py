# ==================================================
# ==================================================
#    Inheritence, Polymorphism, Magic Methods
# ==================================================
# ==================================================

# Super Class
# Sub Class

# Inheritence: a way of using fields and methods,
# from a super class into sub class

# Magic Method: The methods that allows us to use built in function
# of python on our classes or objects
# Example : print(Class_Name) Should print info related to class.
# Example : sum([rect1, rect2]) should add rectangle 1 and rectangle 2.
# The magic methods are described in the class body
# The methods starts with two underscores and end with two underscores


# =====================================
# Create a class Animal that has common properties of every animal
# Then create a reptiles class that inherits animal class
# Now use methods and fields of animal class in mammal class
# Use __str__ magic method in animal class and override in mammal class
# Use super method in override method to get exact str of
# animal class and append their nurseYoung status

#
# Hints:
# Fields of Animal : birthType="Unknown...",
#                   appearence="Unknown", blooded="Unknown"

# Fields of Mammal : birthType="born alive",
#                   appearence="hair or fur", blooded="warn blooded", nurseYoung=True

# Fields of Reptile class: birthType="born in an egg or born alive",
#                    appearence="dry scales", blooded="cold blooded", nurseYoung=True


# Defining an animal class
class Animal:

    # Defining the initialization method
    def __init__(self, birthType="Unknown", appearence="Unknown", blooded="Unknown"):
        self.birthType = birthType
        self.appearence = appearence
        self.blooded = blooded

    @property
    def birthType(self):
        return self.__birthType

    @birthType.setter
    def birthType(self, birthType):
        self.__birthType = birthType

    @property
    def appearence(self):
        return self.__appearence

    @appearence.setter
    def appearence(self, appearence):
        self.__appearence = appearence

    @property
    def blooded(self):
        return self.__blooded

    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded

    # Defining a string magic method
    def __str__(self):
        return "A {} is {} it has {} it is {}".format(type(self).__name__,
                                                     self.birthType,
                                                     self.appearence,
                                                     self.blooded)


# Creating a mammal class that inherits animal class
class Mammal(Animal):

    # Defining Initialization method
    def __init__(self, birthType="born alive",
                 appearence="hair or fur",
                 blooded="warm blooded",
                 nurseYoung=True):
        # Initializing Animal Class
        Animal.__init__(self, birthType, appearence, blooded)

        self.__nurseYoung = nurseYoung

    @property
    def nurseYoung(self):
        return self.__nurseYoung

    @nurseYoung.setter
    def nurseYoung(self, nurseYoung):
        self.__nurseYoung = nurseYoung

    # Overriding a method
    def __str__(self):
        return super().__str__() + " and it is {} that they nurse " \
                                   "their young".format(self.__nurseYoung)


class Reptile(Animal):

    def __init__(self, birthType="born alive",
                 appearence="hair or fur",
                 blooded="cold blooded"):
        Animal.__init__(self, birthType, appearence, blooded)


def main():
    # Create an animal and print its birthType
    animal1 = Animal("born alive")
    print(animal1.birthType)

    # Calling our str magic method
    print(animal1.__str__())

    print("="* 20)

    # Creating a mammal animal
    mammal1 = Mammal()

    # Access Fields of mammal
    print(mammal1.birthType)
    print(mammal1.appearence)
    print(mammal1.blooded)
    print(mammal1.nurseYoung)

    # Access str magic method on mammal class
    print(mammal1.__str__())
    print(mammal1)

    # Print a line to seperate content
    print("=" * 20)

    # Creating a reptile class
    reptile1 = Reptile()

    # Printing Fields of reptile class
    print(reptile1.birthType)
    print(reptile1.appearence)
    print(reptile1.blooded)

    # Access string magic method
    print(reptile1)


if __name__ == '__main__':
    main()


# ===============================================
# Polymorphism: Poly means many, and morphism means forms
# hence polymorphism is a way to define any object with properties
# and use it as long as its fields or methods used in class exists

# In other languages such as c++, c# there is a concept of
# statically typed language that is we need to define datatype of variable
# before assigning it some value. As python is dynamically typed language
# we do not need to specify datatype of variable. it is inferred automatically

# Polymorphism: An object is passed to the function or class. You can use the
# object and its fields and methods if the passed object holds those in
# use fields and methods



# Example to demonstrate this concept :
# Create a function called as tell_me(someObject), here someObject is a
# variable that will be passed to the function
# Implement the function to print Class Name and someObject.birthType
# Inside main Call the function passing reptile and mammal object.

def tell_me(someObject):
    print("Class Name: {} and birthType: {}".format(type(someObject).__name__, someObject.birthType))


def main():
    # Creating reptile and mammal object
    reptile1 = Reptile()
    mammal1 = Mammal()

    # Calling tell_me function to print class name and birth type
    tell_me(reptile1)
    tell_me(mammal1)

    # # Calling tell_me function with a invalid object
    # tell_me(None)   # The line throws an error
    # tell_me("Hello") # the line throws an error due to unavailability of birthType


main()


# ======================================================
#                   Magic Methods
# ======================================================

# Magic Methods : the special kind of methods that are used to
# define custom behaviour of some operator, method or object

# Properties:
# They start and end with two underscores

# They do not need to be invoked as other function: reptile1 + reptile2
# In above line + is defined a custom behaviour
# to add reptile1 and reptile2 using __add__ magic method

# Some Magic methods:
# __eq__ : equal
# __ne__ : not equal
# __lt__ : less than
# __gt__ : greater than
# __le__ : less than or equal to
# __ge__ : greater than or equal to
# __add__ : addition
# __sub__ : subtraction
# __mul__ : multiplication
# __div__ : division
# __mod__ : modulus



# ==========================================================
# Create a Time class with fields hour min sec
# Implement the add magic method to add two times
# Implement the string magic method to return time as 02:03:10 string
# The time class with work with 24 hour time

# Sample output:
# Time 1: 23:10:52
# Time 2: 23:05:15
# Added time: 22:16:07


# Creating a class
class Time:

    # Defining the class initialization method
    def __init__(self, hour=0, min=0, sec=0):
        self.hour = hour
        self.min = min
        self.sec = sec

    def __str__(self):
        return "{:02d}:{:02d}:{:02d}".format(self.hour, self.min, self.sec)


    def __add__(self, otherTime):
        newTime = Time()

        # Adding of hour min and sec
        newTime.hour = self.hour + otherTime.hour
        newTime.min = self.min + otherTime.min
        newTime.sec = self.sec + otherTime.sec


        # Compare if the hour is greater than 24
        if newTime.hour >= 24:
            newTime.hour -= 24

        # Compare if the min is greater than 60
        if newTime.min >= 60:
            newTime.hour += 1
            newTime.min -= 60

        # Compare if the sec is grater than 60
        if newTime.sec >= 60:
            newTime.min += 1
            newTime.sec -= 60

        # returns newtime
        return newTime


def main():
    # Creating time1 and time2 objects
    time1 = Time(23, 10, 52)
    time2 = Time(23, 5, 15)

    # Testing str method
    print("Time 1:", time1)
    print("Time 2:", time2)

    # Testing add operator
    print("Added time:", time1 + time2)

main()



