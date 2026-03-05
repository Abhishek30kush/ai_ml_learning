# # set1={"avinash", "ravi", 'vinay'}
# set1 = {"abc", 34, True, 40, "male"}
# # print(len(set1))
# # set2={1, 5, 7, 9, 3}
# # set3={True, False, False}
# print(set1)
# # print(set2)
# # print(set3)
# # print(type(set2))


# print(thisset)
# print(type(thisset))
# for x in thisset:
#     print(x)

# print("banana" not in thisset)
# thisset = set(("apple","banana", "cherry"))

# thisset.add("orange")
# mylist=['kiwi', 'orange']
# # del thisset
# # print(thisset)
# thisset={"pineablle", "mango", "papaya"}

# for x in thisset:
#     print(x)z

# set1={'a', 'b', 'c', 'd', 'e'}
# set2={1, 2, 3, 4}

# set3=set1 | (set2)
# print(set3)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}
# y=('name', 'game', 'fame')
# z=set1.union(y)
# print(z)
# myset = set1.union(set2, set3, set4)
# print(myset)

set1 = {"a", "b", "c", 1, True, False}
set2 = {"ab", "cb", "b", 'a', 1, 0}
# set1.intersection_update(set2)
# print(set1)

# set3=set1^(set2)
# print(set3)

set1.symmetric_difference_update(set2) 
print(set1)