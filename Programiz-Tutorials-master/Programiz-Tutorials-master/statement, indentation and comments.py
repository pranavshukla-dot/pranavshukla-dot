'''
End of a statement is marked with a newline character. Statment can be extended over multiple lines using the
continuation character
'''
num = 1 + 2 + 3 + \
      4 + 5 + 6 + \
      7 + 8 + 9
print num

# continuation is implied inside parentheses (), brackets [] and braces {}
num2 = (1 + 2 + 3 +
        4 + 5 + 6 +
        7 + 8 + 9)
print num2


# DOCSTRING

def testFunction():
    """
    This function does nothin
    :return: None
    """
    print 'Nothing'

# The docstring is available for us as the __doc__ attribute of a function
print testFunction.__doc__