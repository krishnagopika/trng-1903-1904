# from package import *

# print(fact.factorial(10,4))

class Vampire:

    _name = "some name"

    value = "Some text"

    def __init__(self) -> None:
        pass

    def description(self):
        return "Cold Blooded"

class Wearwolf:

    def __init__(self) -> None:
        pass

    def hunt(self):
        return "We hunt vampires"

class VampireWearwolf(Vampire, Wearwolf):

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name


klaus = VampireWearwolf("Klaus")

vamp = Vampire()
print(vamp._name)

print(klaus._name)

print(klaus.description(), klaus.hunt())