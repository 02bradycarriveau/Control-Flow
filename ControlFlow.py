"""
Programmer: Brady Carriveau
Date: 12/16/19
Program: Guess my number

Number2 = 14
myNumber = 7
Number3 = 26
print("\nGuess a number between 1 & 10\n")


# aks users to guess
guess = int(input("\nEnter a Guess\n"))

#ask person until they get it right
#it is equal to myNumber
while guess != myNumber:
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

"""
Programmer: Brady Carriveau
Date: 12/19/19
Program: 1-10
"""


x = 1

#While loop will see if a condition has been met
# If not it will run again the condition
# has been met

while x <= 10:
    print(x)
    x = x + 1