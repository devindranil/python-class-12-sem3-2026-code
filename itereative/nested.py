# nested loop
# example 1
# multiplication table

# Outer Loop
'''for i in range(2,6):
    print(f"\nTable of {i}")
    # nested loop - Inner loop
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")'''

# Example 2
# VVI Practical
'''
    Pattern print
    triangle pyramid (Half pyramid)

    *
    *   *
    *   *   *
    *   *   *   *
    *   *   *   *   *

'''
'''
    formula
    row=1, value=1
    row=2, value=2
    row=3, value=3
    row=4, value=4
    row=5, value=5
    .
    row=6, value=6
    .
    .
    row = value

'''
# outer loop = i where no of rows in the pattern
'''for i in range(1,6):
    # Inner loop represent the actual number of value or column
    for j in range(i):
        print("*",end=" ")
    print()'''

'''
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''
'''for i in range(1,6):
    # Inner loop represent the actual number of value or column
    for j in range(i):
        print("*",end=" ")
    print()'''

# Full pyramid
'''
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 

'''
rows=5
for i in range(1,rows+1):
    # print spaces
    for j in range(rows-i):
        print(" ",end=" ")
    # print number of star
    for k in range(2*i-1):
        print("*",end=" ")
    print()