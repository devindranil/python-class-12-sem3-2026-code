# what is string in python ?
# ans = string is a sequence of more than one character
# string are represented by single/double/tripple quotation in python
# anything inside the quotation is consider as a string, exam "123"->str class
# string is immutable data type or data structure
# string memory is similar to list or array in computer programming, exaample-"India"
'''
    String memory
    "India"
    Range = 0 to n-1
    0   1   2   3   4
    I   n   d   i   a
'''

# string declaration
student_name = "Rahul" # double quotation
school = 'ABC High School' # single quotation
address = """123, Street Name,
Kolkata, West Bengal""" # Multi-line string

'''print(student_name)
print(school)
print(address)'''

# Basic String operation

# String concatenation(+)
first_name="Indranil"
last_name="Chakraborty"
full_name=first_name + " " + last_name #concatenate
#print(full_name)

# String Repetition(*)
name="Lionel messi" + " "
#print(name*5)

# Membership operator(in and not in) - any sequence type object, case sensitivity
sentence = "Python is very easy to learn."
'''print("Easy" in sentence)     # Output: False
print("Java" not in sentence)  # Output: True'''

# VVI - String slicing
# Formula: string[start_index : end_index : step], end_index=end_index-1

msg = "Python"
'''
    0   1   2   3   4   5 - Positive index
    P   y   t   h   o   n
    -6  -5  -4 -3  -2  -1 - Negative index, range=-1 to -n
'''

# String slicing
'''print(msg) # Python
print(msg[0:2]) # Py
print(msg[2:]) # thon, when only start index present and no end index then python print the value till the last character of the string memory
print(msg[:4]) # Pyth, when only end index present and no start index then python print the value from the 0th index character of the string memory and stop at end index -1 position
print(msg[1]) # y, when only one value that time that particul;ar index item will be print
print(msg[-1]) # n
print(msg[::2]) #[::step] Pto
print(msg[1:4:2]) # yh
print(msg[::-1]) # Reverse order nohtyP'''

# Traversing algorithm 
# using loops in string to itereate every charcater and display

# using for loop
'''word = input("Enter any word: ")
for char in word:
    print(char, end=" ,") # ques=is the seprator added onto last item = yes

print() 

word1 = input("Enter any word: ")
for char in word1:
    print(char, end="")

print()

word2 = input("Enter any word: ")
for char in word2:
    print(char)'''

# using range() and len()
'''word = input("Enter any word: ")
for i in range(len(word)):
    print(f"Index {i} occupies character: {word[i]}")'''

# Built-in function in string
#print(len("Python")) # return the total length of string memory
# print("viRat Kohli".capitalize()) # (case 1): if no chracter is upper case then convert the first character into upper case and rfemaining all character remain same  (case 2) if any one character is in upper case then it's always convert them into lower case except the 0th position

#print("ROhit shArma".title()) # first letter of every word convert into upper case , if any chracter is upper case except the first charcter of the words then it's convert into lowercase

'''print("indrANil".upper()) #convert each charcater into upper case
print("CHAKRabORTY".lower()) #convert each charcater into lower case'''

# Next class = Searching and checking methods
text = "I Love Python Programming. Python is Fun"

# 1.count() - return no of times a char or a word is repeat in the particular string
# print(text.count("P"))

# 2.find() - return the position index of any charcater in the string
'''print(text.find("Python")) # output 7
print(text.find("Love")) # output 2
print(text.find("P")) # output 7
print(text.find("Java")) # Missing or not present in string memory, then find return -1
print(text.find("x"))'''

# 3.index() = similar to find() only difference is index return error when a character or word does't present in string memory
# print(text.index("Python")) # output 7
# print(text.index("Java")) # valueError: substring not found

# 4. startswith() and endswith() = return True or False
'''msg = "assignment.docx"
print(msg.startswith("A"))
print(msg.endswith("pdf"))'''


# Type checking methods - return True or False
'''print("Python3".isalnum()) # True (Alphabets + Numbers both are present)
print("India".isalnum()) # True (If only alphabets then also return True)
print("12345".isalnum()) # True (If only numbers then also return True)
print("@@@@&&&".isalnum()) # False (If only special charcater then return False)
print("India@@@@&&&123".isalnum()) # False (If any one charcater is speical symbols then it's always return False)'''

'''print("Python".isalpha()) # True (If only alphabets are present and no numbers and no spaces are present)
print("Python3".isalpha())
print("I Love You".isalpha())'''

'''print("12345".isdigit()) # True (If all chracter is digit)
print("1 2345".isdigit()) # False (If any spaces include)
print("123Python".isdigit()) # False (If any alpahbet include)'''

'''print("python".islower()) # True (If all charcater is lowercase)
print("Python".islower())  # False (If any one charcater is uppercase)
print("i love india".islower()) # True (it's does't matter a white space present or not)'''

# print("PYTHON".isupper()) # True (If all chracter is uppercase)
# print("PYTHON iS".isupper())

'''print("   ".isspace()) # True (If only white spaces are present)
print("I Love Programming".isspace()) # False (because not all ch is white space)'''

# String stripping and modifying methods
'''msg = "    hello    "
print(msg)
# Left strip -> "hello    "
print(msg.lstrip())
# Right strip -> "    hello"
print(msg.rstrip())
# Both side -> "hello"
print(msg.strip())'''

# replace() in python
'''msg = "I Like Java"
print(msg)
x=msg.replace("Java","Python")
y=msg.replace("Like","Love")
print(x)
print(y)
print(id(msg))
print(id(x))
print(id(y))'''

# vvi = replace create a new string

# string splitting, joining and partitioning

# all this method create a new memory

# 1.split() - convert any string items into list
'''data = "Rahul,amit,subham"
student_list = data.split(",")
print(data)
print(student_list)
print(len(student_list))'''

# 2. join() - convert any list items into a string
'''names = ["Sayak", "Eshita", "Bidisha"]
res = ", ".join(names)
print(res)'''

# 3. partition()
email = "support@gmail.com"
msg=email.partition(".")
print(email) 
print(msg)

# imp = return tupple and partition into three part (before, exact, after), new memory crete