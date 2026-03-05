import functools

def changecase(func):
  @functools.wraps(func)
  def dinner():
    return func().upper()
  return dinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)