# thistuple = ("apple", "banana", "cherry", "cherry")
# print(len(thistuple))

# thistuple = ("apple",)
# print(type(thistuple))

# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))

# mytuple = ("apple", "banana", "cherry")
# print(type(mytuple))

# thistuple=tuple(("apple", 'banana', 'cherry'))
# if 'banana' in thistuple:
#     print("yes")

# x = ("apple", "banana", "cherry")
# y = list(x)
# y.append("kiwi")
# x=tuple(y)
# print(x)

# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)

# thistuple=('abhi', 'kabhi', 'tabhi')
# y=list(thistuple)
# y.remove('tabhi')
# thistuple=tuple(y)
# # print(thistuple)

# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)