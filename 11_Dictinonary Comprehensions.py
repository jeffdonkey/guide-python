
# DICTIONARYs can be generated in comprehensions

# syntax
# dict = {key:expression for element in iterable}
    # dict = the variable to save the list to
        # DOES NOT HAVE TO BE THE EXACT WORD DICT
    # {} = encases
    # expression = what to name the key and
        # what to do to the element before
        # saving it    
    # for...in loop = loop through the iterable
        # to make the new dintionary
    

# example
dict = {num: num * 2 for num in range(4)}
    # output {0:0, 1:2, 2:4, 3:6}

# when you access the DICTIONARY through "print" or any other way the program
    # would access the DICTIONARY the data will match the EXPRESSION