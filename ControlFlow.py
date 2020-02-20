# Program: Guess my number
#Date: 12/16/19
#Programmer: Brady Carriveau
#Program: Guess my number
Number2 = 14
myNumber = 7
Number3 = 26
print("\nGuess a number between 1 & 10\n")


# aks users to guess

guess = int(input("\nEnter a Guess\n"))

#ask person until they get it right
while guess != myNumber:
#it is equal to myNumber
    print("\nnope, not right. again?")
    guess = int(input("enter a guess:"))


print("\nWhoa, you got it right\n")
print("\nGuess a number between 1 & 20\n")



guess = int(input("\nEnter a Guess\n"))

while guess != Number2:
    print("\nnope, not right. again?")
    guess = int(input("enter a guess:"))

print("\nWhoa, you got it right again!\n")


print("\nGuess a number between 1 & 100\n")


guess = int(input("\nEnter a Guess\n"))

while guess != Number3:
    print("\nnope, not right. again?")
    guess = int(input("enter a guess:"))

print("\nYour the ultimate guesser!\n")


"""
Programmer: Brady Carriveau
Date: 12/19/19
Program: 1-10
"""

#Programmer: Brady Carriveau
#Date: 12/19/19
#Program: 1-10



x = 1

#While loop will see if a condition has been met
# If not it will run again the condition
# has been met

while x <= 10:
    print(x)
    x+=1

# programmer Brady Carriveau
#Date: 1.20.20
# progam: Double For Loop


for i in range(3):
    print("Outer For Loop" + str(i))
    for k in range(4):
        print("\tInner for loop" + str(k))


print ("\n*************************************\n")
"""
Programmer: Brady Carriveau
Date: 1.23.20
program While loop nested inside for loop
"""



for i in range(4):
    print("For Loop:" + str(i))
    x = i
    while x >= 0:
        print("\t While Loop: " + str(x))
        x = x - 1


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

#Print Sum
def printSum(x,y):
    print(x + y)

#Print SUm multiple times
def printSumMulitpleTimes(string, times):
    for i in range(times):
        print(string)
# Call Functions Here

#greeting()
#printSomething()
#print(x)
#printNumber(26)
#printNumber(15)
#printTwoNumbers(23,20)
#printTwoNumbers(3)
#printSum(1,17)
printSumMulitpleTimes("I love CS!", 10000000000)