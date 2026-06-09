# for loop examples

'''
syntax
sequence = list,string,sets,dict,range()

for loop_variable in sequence:
    -- loop body
    // write the statement

'''

# Example 1
'''fruits=["apple","mango","orange","banna","guava"]

for x in fruits:
    print(x)'''

'''
1st = apple
2nd = mango
3rd = orange
4th = banana
5th = guava

How many number of times this loop itereate or execute ? = 5 times
'''

# Example 2
# WAP in python to input your name and find out which charcater is vowel and which is not a vowel

# user input
'''name=input("Enter your Name: ")
for ch in name:
    # print(ch)
    # condition to check a character is vowel or not
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u" or ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U":
        # f string
        print(f"The charcter:{ch} is vowel...")
    else:
        print(f"The charcater:{ch} is not a vowel")'''

# Example 3
# WAP in python to calculate total marks from a list
marks=[95,85,99] #marks list
total=0 #every iteretaion value update
for m in marks:
    total=total+m
print("Total marks of 3 subject is: ", total)

'''
total=0 -> 95 -> 180 -> 279
1st itereation = m=95 total=0+95=95
2nd itereation = m=85 total=95+85=180
3rd itereation = m=99 total=180+99=279
print(total) = 279
'''