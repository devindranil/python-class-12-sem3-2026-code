#list declare
'''numbers=[10,20,30,40,50]
mixed_lits=[1,"Rahul",3.14,True]
empty_list=[]

print(numbers)
print(mixed_lits)
print(empty_list)'''

#indexing in list
numbers=[10,20,30,40,50]
mixed_lits=[1,"Rahul",3.14,True]

'''print(numbers[3]) #40
print(mixed_lits[-2]) #3.14
print(numbers[6]) # Run Time error (IndexError: list index out of range)'''

# MUTABLE
'''print(numbers)
numbers[3] = "India"
print(numbers)'''

# List Operation

# concatenation (using + operator)
list1=[1,2,3]
list2=[10,True,"India"]

'''newlist=list1+list2
print(id(list1))
print(id(list2))
print(id(newlist))'''

# 2.List Repetition
#print(["India",10]*4) # create a new memory

# 3.Membership operator(in, not in)
'''print("green" in list2)
print("india" not in list2)'''

# 4.slicing
nums=[10,20,30,40,50,60,70,80,90,100]

#[start:stop], stop=stop-1
'''print(nums[1:4]) # [20,30,40]
print(nums[:3]) #[10,20,30]
print(nums[1:4:2]) # [20,40]'''
'''
    20 = print
    30 = not print
    40 = print
'''

#print(nums[:9:1])
'''
 when the step value is 1 then all items will be print
    10 = y
    20 = n
    30 = n
    40 = y
    50 = n
    60 = n
    70 = y
    80 = n
    90 = n
'''

#print(nums[:9:3])

# reverse a list
#print(nums[::-1])

# Traversing a list using loops
'''names = ["Amit", "Sumit", "Rohit"]
for i in names:
    print("Welcome ",i)'''


# Built-in Functions & Methods
my_list = [1, 2, 3]

# 1. append() - লিস্টের একদম শেষে একটি মাত্র আইটেম যোগ করে
'''print(id(my_list))
my_list.append(4)
print(id(my_list))'''

# 2. insert() - নির্দিষ্ট ইনডেক্সে জোর করে আইটেম ঢুকিয়ে দেয় -> insert(index, item)
'''print(my_list)
my_list.insert(1,"YCH")
print(my_list)'''

# 3. extend() - অন্য একটি পুরো লিস্ট বা কালেকশনকে শেষে জুড়ে দেয়
print(my_list)
my_list.extend({"name":"Indranil","year":2026}) #only key 
my_list.extend([5,6,7]) 
print(my_list)

# Removing Items



# Searching & Counting


# Sorting & Reversing


# Mathematical Functions & Type Casting


# Nested Lists