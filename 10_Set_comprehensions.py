# SETs are used to store multiple items in a single variable
# SETs can be generated in comprehensions

# syntax
# set = {expression for element in iterable if...}
    # set = the variable to save the list to
        # DOES NOT HAVE TO BE THE EXACT WORD SET
    # {} = encases
    # expression = what to do to each element before
        # BEFORE putting it in the list
    # for...in loop = loop through the iterable
        # make the new set
    # if... = optional expression to filter the elements

# example
divisible = {num for num in range(10) if num % 2 == 0}
    # output {0,2,4,6,8}

# when you access the SET through "print" or any other way the program
    # would access the SET the data will match the EXPRESSION