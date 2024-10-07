from __future__ import print_function

# DEFAULT ARGUMENTS
def greet(name, msg = "good morning!"):
   """This function greets to
   the person with the provided message.
   If message is not provided, it defaults
   to "Good morning!" """

   print("Hello",name + ', ' + msg)

greet('Kate')
greet('Bruce','how do you do?')


# non-default arguments cannot follow default arguments. that is to say, the following would not be allowed:
# def greet(msg = "good morning", name):


# ARBITRARY ARGUMENTS: defined using asterisk (*)
def greet(*names):
   """This function greets all
   the person in the names tuple."""

   # names is a tuple with arguments
   for name in names:
       print("Hello",name)


greet("Monica","Luke","Steve","John")