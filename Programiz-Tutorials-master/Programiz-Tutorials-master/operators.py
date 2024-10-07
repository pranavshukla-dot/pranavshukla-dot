from __future__ import print_function, division

print('ARITHMETIC OPERATORS')
x = 15
y = 4
print('x + y = ',x+y)
print('x - y = ',x-y)
print('x * y = ',x*y)
print('x / y = ',x/y)               #division always results in a float (real division)
print('x // y = ',x//y)             #floor division (classic division as in Python 2)
print('x ** y = ',x**y,end='\n\n')


print('COMPARISON OPERATORS')
x = 10
y = 12
print('x > y  is',x>y)
print('x < y  is',x<y)
print('x == y is',x==y)
print('x != y is',x!=y)
print('x <> y is',x<>y)             #alternative way to do 'not equal'comparison
print('x >= y is',x>=y)
print('x <= y is',x<=y,end='\n\n')


print('LOGICAL OPERATORS')
x = True
y = False
print('x and y is',x and y)
print('x or y is',x or y)
print('not x is',not x,end='\n\n')

print('BITWISE OPERATORS')
x = 10  # 0000 1010 in binary
y = 4   # 0000 0100 in binary

print('x AND y is',x & y)    # AND: 0000 0000
print('x OR y is',x | y)    # OR:  0000 1110
print('NOT x is',~ x)      # NOT: 1111 0101
print('x XOR y is',x ^ y)    # XOR: 0000 1110
print('x shifted right by two bits is',x >> 2)   # Bitwise shift right: 0000 0010
print('x shifted left by two bits is',x << 2,end='\n\n')   # Bitwise shift left:  0010 1000

print('IDENTITY OPERATORS')
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
print(x1 is not y1)
print(x2 is y2)
print(x3 is y3,end='\n\n')

print('MEMBERSHIP OPERATORS')
x = 'Hello world'
y = {1:'a',2:'b'}
print('H' in x)
print('hello' not in x)
print(1 in y)
print('a' in y)