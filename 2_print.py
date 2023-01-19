# print is equalivent to console.log
# print is a built in Python FUNCTION that prints to the standard output device (display monitor)

print("hello")

# in the example below a 'f-string' is used in the print agrument
# is also called 'f-strings' that are used in print
# these 'f-strings' are used to print concat's as strings
# without the need for older python formating.

name = "Tom"
job = "waiter"
print(f"Hello, {name}. You are a {job}")


# the syntax for print changes a bit depending on the argument data

print(42)                           # int - integer
print(3.14)                         # float - floating decimal place
print('hello')                      # str - string
print(True)                         # bool - boolean
print([1,2,3])                      # list
print((1,2,3))                      # tuple
print({'red','blue','green'})       # set
print({'name': 'Jon', 'age': 22})   # dict - dictionary - key:value pairs