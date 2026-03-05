def changecase(func):
  def myinner():
    print("Changing case...")   
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    print("Adding greeting...")
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Tobias"

print(myfunction())