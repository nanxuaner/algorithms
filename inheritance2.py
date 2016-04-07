class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        print ("We got a new pet %s" %(self.name))

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self):
        return "The pet %s is a %s" %(self.name, self.species)

class Dog(Pet):
    def __init__(self, name, chases_cats):
        Pet.__init__(self, name, "Dog")
        self.chases_cats = chases_cats

    def chasesCats(self):
        return self.chases_cats

class Cat(Pet):
    def __init__(self, name, hate_dogs):
        Pet.__init__(self, name, "Cat")
        self.hate_dogs = hate_dogs

    def hateDogs(self):
        return self.hate_dogs



def testInheritace1():

    r = Pet("pop", "rabbit")
    d = Pet("bob", "dog")
    members = [r, d]
    for member in members:
        print ("%s is a %s" % (member.getName(), member.getSpecies()))

#testInheritace1()


def testInheritance2():
    apple = Dog("apple", True)
    pear = Dog("pear", True)
    pitch = Dog("pitch", False)
    Tobby = Cat("Tobby", True)
    Andraw = Cat("Andraw", True)
    Cici = Cat("Cici", False)

    dogs = [apple, pear, pitch]
    cats = [Tobby, Andraw, Cici]
    pets =[apple, pear, pitch, Tobby, Andraw, Cici]
    for pet in pets:
        print ("%s is a %s" %(pet.name, pet.species))
    for dog in dogs:
        print ("%s chases cats %s" %(dog.name, dog.chasesCats()))
    for cat in cats:
        print ("%s hates dogs %s" %(cat.name, cat.hateDogs()))

testInheritance2()