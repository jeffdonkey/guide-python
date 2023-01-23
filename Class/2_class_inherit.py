## stated this with instruction from https://realpython.com/python3-object-oriented-programming/
## using material from YouTube creator Corey Schafer and his series on Python OOP
## using various other resources

# this section will cover INHERITANCE.  INHERITANCE is the process by which one class can take attributes 
    # from another class.  Think of this as a child-parent relationship.


# STARTING CODE:

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

# Next step: we will add three new classes that match dog breeds.  Each one will contain a method called 'speak'.

class JackRussellTerrier(Dog):
    def speak(self, sound='Arf'):
        return f"{self.name} says {sound}"

class Dachshund(Dog):
    def speak(self, sound='Woof'):
        return f"{self.name} says {sound}"

class Bulldog(Dog):
    def speak(self, sound='snort'):
        return f"{self.name} says {sound}"

    # in each of these new classes the argument used in the class Dog.  These classes will share instance data from class Dog.

# Now will will instanciate some instances.  Note we are setting the variables to different classes but also sending arguments
    # that will be used in class Dog.

miles = JackRussellTerrier("Miles", 4, "Jack Russell Terrier")
buddy = Dachshund("Buddy", 9, "Dachshund")
jack = Bulldog("Jack", 3, "Bulldog")
jim = Bulldog("Jim", 5, "Bulldog")

# Look at this print statement:

print(miles.speak())

    # when the print is ran you will display 'Miles says Arf'.  

