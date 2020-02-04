
# Date: 2.3.20
#Programmer: Brady Carriveau


# Global Variables
#name = input("What is your name:  ")
x = 15

# Create Functions Here

# Greeting Function
def greeting():
    print("Hi there "   +   name + "!")
    print("Very Nice to met you " + name)
    print(x)
# Functions and local variables  X
def printSomething():
    x = 3
    print(x)


# functions and parameters
def printNumber(age): # Function name = printNumber with a parameter of age
    print(age)

# Default Parameter Values
def printTwoNumbers(x,y = 17):
    print("First Parameter(Number): " + str (x))
    print("First Parameter(Number): " + str (y))
# Call Functions Here

#greeting()
#printSomething()
#print(x)
#printNumber(26)
#printNumber(15)
printTwoNumbers(23,20)
printTwoNumbers(3)