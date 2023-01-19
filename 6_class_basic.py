## stated this with instruction from https://realpython.com/python3-object-oriented-programming/
## using material from YouTube creator Corey Schafer and his series on Python OOP
## using various other resources


# Classes are used to create data structures used in Object-Oriented Programming (OOP) in Python.
# A class is a blueprint for how something should be defined.
# It does not actually contain any data.
# An 'INSTANCE' is an object that is built from a class and contains real data.

# Think of 'class' as a questionnaire.  Think of instance is the same questionnaire with the blanks filled-in.

class SomeDogs:
    def speak(self):
        print('woof')

# Classes are declared by using the keyword 'class'.  The name of the class should be capitalized.
# Functions used within a class are called 'METHODS'.

#-----------------------------------------------------------------------------------------------------------

# CLASS EXAMPLE START:

class Dog:
    pass

    # on line 17 the 'pass' keyword is used.  Python recognizes 'pass' as a placeholder.

#-----------------------------------------------------------------------------------------------------------

# '.__init__()' METHOD

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # line 26 uses the '.__init__()' method. Every time a new 'Dog' object is created, '.__init__()'
        # sets the initial STATE of the object by assigning the values of the object's properties.
        # '.__init__()' initializes each new instance of the class.
        # '.__init__()' canhave any number of parameters , but the first parameter will always be
        # a variable called 'self'.  When a new class instance is created, the instance is automatically
        # passed to the 'self' prarmeter in '.__init__()' so that the new ATTRIBUTES can be defined
        # on the object.
    # line 27 'self.name = name' creates an ATTRIBUTE called 'name' and assigns to it the value of the 
        # 'name' PARAMETER.
    # line 28 'self.age = age' creates an ATTRIBUTE called 'age' and assigns to it the value of the
        # 'age' PARAMETER.
    # ATTRIBUTES created in '.__init__()' are called 'INSTANCE ATTRIBUTES'.  This means that an 'INSTANCE ATTRIBUTE'
        # is specific to a particular instance of the class.  All 'Dog' object instances will have a 'name' and 'age'
        # but the values of 'name' and 'age' will change according to the instance.

#--------------------------------------------------------------------------------------------------------------

# CLASS ATTRIBUTES

class Dog:

    species = 'Canis Familiaris'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # line 49 is a 'CLASS ATTRIBUTE'.  A 'CLASS ATTRIBUTE' has the same value for all object instances.

#-----------------------------------------------------------------------------------------------------------

# INSTANCE AND INSTANCIATION

class Dog:

    species = 'Canis Familiaris'

    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog('Lottie', 6)
dog2 = Dog('Sampson', 9)

    # lines 69-70 each create an INSTANCE of the class 'Dog'.  Doing this is called INSTANTIATION.  When 
        # INSTANTIATION is done there is a space in computer memory assigned to each instance.
        # When you pass in the data to the class you do not have in include 'self'.

#-------------------------------------------------------------------------------------------------------------

# using DOT NOTATION to access the CLASS INSTANCE

class Dog:

    species = 'Canis Familiaris'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
dog1 = Dog('Lottie', 6)
dog2 = Dog('Sampson', 9)

print(dog1.name)  # will display 'Lottie'

    # line 90 uses DOT NOTATION to access the CLASS INSTANCE for 'dog1'.  SYNTAX: instance_name.class_instance_attribute

#--------------------------------------------------------------------------------------------------------------------------

# Creating an attribute within the class by combining received arguments

class Dog:

    species = 'Canis Familiaris'

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.fullname = firstname + ' ' + lastname
        
dog1 = Dog('Lottie', 'Spottygirl', 6)
dog2 = Dog('Sampson', 'Goodboy', 9)

print(dog2.fullname)  # will display 'Sampson Goodboy'

    # made changes to this example code to use a first name and last name.
    # line 116 sets an class attribute called 'fullname'.


#--------------------------------------------------------------------------------

# Multiple METHODS (functions) within a CLASS

class Dog:

    species = 'Canis Familiaris'

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)
        
        
dog1 = Dog('Lottie', 'Spottygirl', 6)
dog2 = Dog('Sampson', 'Goodboy', 9)

print(dog2.fullname())  # will display 'Sampson Goodboy'

    # lines 141-142 are a second method within the class 'Dog'.  In the method 'fullname' we send in the argument 'self'
        # to tie the insatance of the data received by class 'Dog'.  DOT NOTATION is used to access 'firstname' and 'lastname'
    # line 142: '{} {}' is a placeholder; '.format' will move the values of 'firstname' and 'lastname' into the placeholders.

#-----------------------------------------------------------------------------------------------------------------------

# The '.__str__():' method.

class Dog:

    species = 'Canis Familiaris'

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __str__(self):
        return f'{self.firstname} is {self.age} years old'
      
        
dog1 = Dog('Lottie', 'Spottygirl', 6)
dog2 = Dog('Sampson', 'Goodboy', 9)

print(dog1)  # displays 'Lottie is 6 years old'

    # '.__str__()' is called and DUNDER METHOD due the the double-underscores.  '.__init__()' is also a DUNDER METHOD
        # '.__str__()' is used to make the object returned a STRING

#------------------------------------------------------------------------------------------------------------------------

