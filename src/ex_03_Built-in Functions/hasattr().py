#Check If Object Has Attribute and Checks if an attribute exists.

class Person:
    name = "Amit"

p = Person()
print(hasattr(p, "name"))  # True
print(hasattr(p, "age"))   # False #age is not present
