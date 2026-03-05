class Outer:
  def __init__(self):
    self.name = "Outer Class"

  class Inner:
    def __init__(self, outer):
      self.outer = outer

    def display(self):
      print("This is the inner class")

outer = Outer()
inner=outer.Inner(outer)
inner.display()