# variable : Variables are containers for storing data values.
# creating variable
#reassining variable
# x=5
# x='john'
# print(x)

# casting 

# x=str(3)
# y=int(3)
# z=float(3)
# print(x,y,z)
# getting type 
# print(type(x))
# print(type(y))
# print(type(z))

# camelCase 
# each word, except the first, start with a capital lette: 
# myVariableName ="john"
# print(myVariableName)

# Many values to multiple variables 

# x, y= 3, 6;
# print(x,y);
# x, y= y, x;
# print(x,y) 

# One value to Multiple Variables

# x=y=z="orange"
# print(x,y,z)

# Unpack a collection 
# students = ["Ravi", "Raj", "Ani"]
# x, y, z= students;

# print(y + z + x)


# x=5
# y="Abhi"

# print(x, y)

# Globar Variable
# Variable taht can created outside of a function are known as global variables.
# def myfunc():
#     global x
#     x = "Bye"
#     print(x + " Dosto")
# myfunc()

# print(x  + " Dosto")

# Global Keyword 

# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

# To create a global variable inside a function, you can use the global keyword.

# x = "awesome"
# print (x)
# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# # print("Python is " + x)
# x = 3+5j
# y = 5j
# z = -5j

# print(x)
# print(type(x))
# print(type(y))
# print(type(z))

# import random
# print(random.randrange(1,10))

price = 59
txt = f"The \"price\" is {price+2} dollars"
print(txt)