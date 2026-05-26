# check whether a number is divisible by 5 and 11

num=int(input("Enter a number: "))

# nested if else statement
# outer if
if num%5==0:
    # inner if
    if num%11==0:
        print("Number is divisble by 5 and 11")
    else:
        print("Not divisible by 5 and 11")
else:
    print("Not divisible by 5 and 11")