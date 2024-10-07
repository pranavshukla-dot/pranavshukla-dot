from __future__ import print_function

# An example of a recursive function to
# find the factorial of a number

def recur_fact(x):
   """This is a recursive function
   to find the factorial of an integer"""

   if x == 1:
       return 1
   else:
       return (x * recur_fact(x-1))


num = int(input("Enter a number: "))
if num >= 1:
   print("The factorial of", num, "is", recur_fact(num))


"""
EXPLANATION:

recur_fact(4)              # 1st call with 4
4 * recur_fact(3)          # 2nd call with 3
4 * 3 * recur_fact(2)      # 3rd call with 2
4 * 3 * 2 * recur_fact(1)  # 4th call with 1
4 * 3 * 2 * 1              # retrun from 4th call as number=1
4 * 3 * 2                  # return from 3rd call
4 * 6                      # return from 2nd call
24                         # return from 1st call
"""


"""
Advantages of recursion
    1. Recursive functions make the code look clean and elegant.
    2. A complex task can be broken down into simpler sub-problems using recursion.
    3. Sequence generation is easier with recursion than using some nested iteration.

Disadvantages of recursion
    1. Sometimes the logic behind recursion is hard to follow through.
    2. Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
    3. Recursive functions are hard to debug.
"""