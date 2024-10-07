'''
Syntax of Lambda expressions:   lambda arguments: expression
'''

from __future__ import print_function



# Program to show the
# use of lambda functions

double = lambda x: x * 2
print(double(5))


'''
Use of Lambda function:

We use lambda functions when we require a nameless function for a short period of time. In Python, we generally use
it as an argument to a higher-order function (a function that takes in other functions as arguments). Lambda functions
are used along with built-in functions like filter(), map() etc.
'''


# FILTER FUNCTION:
# The filter() function in Python takes in a function and a list as arguments. The function is called with all the
# items in the list and a new list is returned which contains items for which the function evaluates to True.

# Program to filter out only the even items from a list using filter() and lambda functions
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)


# MAP FUNCTION:
# The map() function in Python takes in a function and a list. The function is called with all the items in the
# list and a new list is returned which contains items returned by that function for each item.

# Program to double each item in a list using map() and lambda functions

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))
print(new_list)



# Own Exercise: Extract all numbers divisable by three
my_list = [1,2,3,4,5,6,7,8,9]
new_list = list(filter(lambda x: (x%3 == 0),my_list))
print(new_list)

# Own Exercise: Add 's' to each entry
my_list = ['one','two','three']
new_list = list(map(lambda x: x+'s',my_list))
print(new_list)
