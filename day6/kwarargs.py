def myfunc(fname, lname):
    print(fname + " " + lname)

person={"fname": "John", "lname": "Doe"}
myfunc(**person)
