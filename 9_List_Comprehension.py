# List Comprehensions are used to generate a list
    # and it's contents at the same time.

# syntax
# list = [expression for element in iterable]
    # list = the variable to save the list to
        # DOES NOT HAVE TO BE THE EXACT WORD LIST
    # [] = encases
    # expression = what to do to each element before
        # BEFORE putting it in the list
    # for...in loop = loop through the iterable
        # make the new list

# example
squared=[num*num for num in range(5)]
    
print(squared) # result would be [0, 1, 4, 9, 16]

# when you access the LIST through "print" or any other way the program
    # would access the LIST the data will match the EXPRESSION

