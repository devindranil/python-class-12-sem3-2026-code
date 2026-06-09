# while loop in python

'''
syntax

loop variable
while condition:
    loop body
    statement
    update the loop variable
'''

# Example 1
# WAP to print a number from 1 to n
'''count=100
while count>=0:
    print("The value of count is: ",count)
    count-=1'''

# Example 2
# Online shopping cart system
'''totalPrice=0 #to calculate the total shopping amount
# Infinite loop
while True:
    item=input("Enter Item price or type done: ")
    if item=="done":
        break
    else:
       totalPrice=totalPrice+float(item) 
print("The total amount is: ",totalPrice)'''

# Example 3
# ATM machine pin
correctPin = "0167"
chances=0
maxchances=3
while chances<maxchances:
    enter=input("Enter your 4 digit atm pin number: ")
    if enter==correctPin:
        print("Access Granted")
        break
    else:
        print("Wrong pin enter: ")
        chances=chances+1
        if chances<maxchances:
            print(f"you have only {maxchances-chances} number of attempt left")
        else:
            print("Your bank account is freeze due to too many incorrect attempt, please visit your nearest bank branch to unfreeze the account, Thank you very much....")
