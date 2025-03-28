"""
import greetings.greetingops
import my_math
import my_math.Arithmetic

print(f"{my_math.Arithmetic.add(2, 3)=}")

from  greetings.greetingops import *
greet()
greetName("Run")

# import greetings
# greetings.greetingops.TestAll()

from  greetings.greetingops import TestAll
greetings.greetingops.TestAll()
"""

# from my_math import add
# from my_math import sine

# print(f"{add(2, 3)=}")
# sine(20)


from my_utils import add

from math import factorial

print(f"{add(2, 3)=}")

# print(dir(__builtins__))
