#! /usr/bin/env python3
# Author: DCameron
# Description: This module contains a collection of calculator functions
"""
    Basic Calculator functions including add, multiply and divide.
"""
import sys

def add(*args):
    """ Return SUM of all parameters """
    total = 0
    for num in args:
        total += num
    return total

def mul(*args):
    """ Return PRODUCT of all parameters """
    total = 1
    for num in args:
        total *= num
    return total

def div(x, z):
    """ Return QUOTIENT of x divided by z to 3 decimal places """
    return round(x/z, 3)

print("Basic Calculator App")

print(f"4 + 3 = {add(4, 3)}")
print(f"4 + 3 + 2 = {add(4, 3, 2)}")
print(f"4 * 3 = {mul(4, 3)}")
print(f"4 * 3 * 2 = {mul(4, 3, 2)}")
print(f"4 / 3 = {div(4, 3)}")

sys.exit(0) # Exit program with 0 errors.