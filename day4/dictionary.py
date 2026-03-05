

# print(type(thisdict['model']))

# thisdict=dict(name="john", age=34, country='Norway')

# x=thisdict.get("model")
# x=thisdict.items()
# print(x)

# if "model" in thisdict:
#     print("yes")

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   'colors': ['red', 'white', 'blue']
  
# }
# # thisdict.clear()
# # print(thisdict)

# # for x, y in thisdict.items():
# #     print(x,y)

# mydict=thisdict.copy()
# print(mydict)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# print(myfamily["child3"]["name"])

for x, obj in myfamily.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])