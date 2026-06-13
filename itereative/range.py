# range() function in python

'''
    use only with for loop
    syntax
    range(start,stop,step)
        start,stop,step both are optional
        range(5) - start 0 and stop n-1, where n is the value , here n=5 so n-1=4
        so the range is 0 to 4
        same way range(10) = 0 to 9

        range(2,6) = start=2 and stop=6 [stop=stop-1] so range = 2 to 5

'''

# example 1
'''for i in range(11):
    print(i)'''

# example 2
'''for i in range(2,6):
    print(i)'''

# example 3 - range with start,stop,step
# STEP MEANS NO OF VALUE SKIPS
'''for i in range(1,15,4):
    print(i)'''

'''
1 = y
2 
3 
4 
5 = y
6 
7 
8
9 = y
10
11
12
13 = y
14
'''

# example 4 - TypeError: range expected at least 1 argument, got 0
'''for i in range():
    print(i)'''

# example 5 - reverse order
'''for i in range(55,0,-1):
    print(i)'''

# example 6 - countdown timer
# import module - time module

# import the required module
'''import time

for second in range(5,0,-1):
    print(f"{second} second remaining")
    # delay = sleep(second)
    time.sleep(2)
print("Your Times Up!!!!")'''

# example 7
# wap in python to check a range of number is even or odd
# n=10, 1 2 3 4 5 6 7 8 9, which are even number and which are odd number

'''n=int(input("Enter the value of n: "))
totalEven=0
totalOdd=0
for i in range(1,n+1):
    # even number
    if i%2==0:
        print(f"The number: {i} is even number")
        totalEven+=1
    else:
        print(f"The number: {i} is odd number")
        totalOdd+=1
print("The total even number is: ",totalEven)
print("The total odd number is: ",totalOdd)'''