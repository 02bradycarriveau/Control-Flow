
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

