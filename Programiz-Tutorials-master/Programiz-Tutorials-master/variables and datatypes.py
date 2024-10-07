# multiple assignments
a, b, c = 5, 3.2, 'hello'
print a,b,c

a = b = c = 'same'
print a,b,c


# numbers in python are defined as either int, float or complex class
a = 5
print type(a)
print type(5.2)
print isinstance(1+2j,complex)

# SETS: since sets are unordered collections, indexing has no meaning. Hence the slicing operator [] does not work
a = {1,2,3}
# print a[0]

# CONVERSION: we can convert from one sequence to another
print set([1,2,3])
print tuple({1,2,3})
print list('hello')

# to convert to dictionary, every element must be a pair
print dict([[1,2],[3,4]])