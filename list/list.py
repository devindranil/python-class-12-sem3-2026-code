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
'''print(my_list)
my_list.extend({"name":"Indranil","year":2026}) #only key 
my_list.extend([5,6,7]) 
print(my_list)'''

# Removing Items
items=["A","B",101,"B",True,"India"]

# 1.remove()
'''print(items)
print(id(items))
items.remove("B")
print(items)
print(id(items))'''

# remove does't create any new list memory.

# 2.pop()
# when you don't provide any index at pop() that time it delete always the last items of that list memory
'''print(items)
print(items.pop(2))
print(items)'''

'''remove=items.pop(1)
print(items)
print(remove)'''

# pop() does't create any new list memory.
# but pop() method always return the deleted items

# Searching & Counting
letters = ["p", "y", "t", "h", "o", "n", "p"]

#len()
'''print(len(letters))
# count()
print(letters.count("p"))
# index()
print(letters.index("h"))'''


# Sorting & Reversing
numbers = [40, 10, 30, 20] #unsorted list

# 1.reverse()
'''print(numbers)
print(id(numbers))
numbers.reverse()
print(numbers)
print(id(numbers))'''

# 2.sort()
'''print(numbers)
print(id(numbers))
numbers.sort() #by default ascending order
print(numbers)
print(id(numbers))
numbers.sort(reverse=True) # descending order
print(numbers)'''

# sort method does not create any new list

# 3.sorted()

'''new_numbers=sorted(numbers)
print(new_numbers)
print(id(new_numbers))
print(numbers)
print(id(numbers))'''

# sorted method create a new list

# Mathematical Functions & Type Casting
# list() - to convert any string into a list we use list() method
'''word = "Indranil Chakraborty"
my_list=list(word)
print(word)
print(my_list)'''

# min(), max(), sum() - only works with numbers
'''val=[10,5,25,5.2,20]
print(min(val)) #return minimum value or the most lowest value
print(max(val)) #return maximum value or the most hihgest value
print(sum(val)) #return the sum of all numbers on the list'''

'''
this function are not work with string or any other type except numbers
example = val=[10,5,25,"A",True,20] 
it's create a TypeError in python
'''
 
# Nested Lists / 2d array / matrix
'''
    3 * 3 order matrix
    row=3 and column=3
    [ 1, 2,  3
     -5, 0,  6
      7, 8,  -1 ]

'''

matrix = [
    [1,2,3], #index=0
    [-5,0,6],#index=1
    [7,8,-1] #index=2
]

'''
    matrix=[
            0 1 2
       0 =  [ 1(0,0) 2(0,1) 3(0,2) ]
       1 =  [ -5(1,0) 0(1,1) 6(1,2)]
       2 =  [ 7(2,0) 8(2,1) -1(2,2)]
    ]

'''

# value access
print(matrix[1])
# print(matrix[row][column])
print(matrix[2][2])

# nested loop
for row in matrix:
    for items in row:
        print(items, end=" ")
    print()