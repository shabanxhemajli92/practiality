

class Person:
    # dunder methods --> double underscore methods
    # self means the "entity" -> self refers to the instance of the class
    def __init__(self, name):
        self.name = name
    def __str__(self) -> str:
        return f"{self.name}"


# "function"
a = Person("Peer")
b = Person("Shaban")
# dot notation
print(a.name)
print(b.name)