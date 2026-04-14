#--Numeric Data Type in Python----
'''x=10
y=3.14
c=2+3j
print("Integer: ",x,"| Type: ",type(x))
print(type(c))'''

#--boolean---
'''isTrue = True
isFalse = False'''

#--usage of boolean in python
'''if 2>1:
    print("It is True")
else:
    print("It is false")

#print(type(isTrue))
#print(type(isFalse))'''

'''text="Python"
print(type(text))
print(len(text))
print(len("I Love Programming"))'''

myList = [10,20,20.55,"India",True,10]
print(myList) #all item access
print(type(myList))
print(len(myList))
print(myList[3]) #one time access
#list is mutable
myList[0]="Youth Career Hub"
print(myList)
# new item insert to the existing list
myList.append(False)
myList.append("West Bengal")
print(myList)
# item remove
myList.remove("India")
print(myList)

