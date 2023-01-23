class Parent:
    def __init__(self) -> None:
        self.value = 10

class Child(Parent):
    pass

child1 = Child()
parent1 = Parent()
print(child1.value)
print(issubclass(Child, Parent))
print(issubclass(Parent, Child))

print(isinstance(child1, Child))
print(isinstance(parent1, Child))
