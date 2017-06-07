class Vehicle:
     def __init__(self):
      self.name = "name"
     
      self.kind = "car"
      self.color = ""
      self.value = 100.00
     def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

car1=Vehicle()
car2=Vehicle()
car1.name="molek"
car1.value=100
car1.kind="van"
car1.color="red"


car2.name="kalmuk"
car2.value=100798797
car2.kind="ufo"
car2.color="rtyyjhj"
print(car1.description())
print(car2.description())




