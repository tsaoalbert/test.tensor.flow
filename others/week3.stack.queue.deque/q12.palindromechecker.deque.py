#!/usr/bin/env python
"""
3.12 Extend the program from Listing 2.15 to handle palindromes with spaces. 
For example, I PREFER PI is a palindrome that reads the same forward and backward if you ignore the blank characters.
"""
from pythonds.basic.deque import Deque
import string

def palchecker(aString):
    aString = aString.translate(None, string.whitespace).upper()

    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))
print(palchecker("I prefer pi"))
print(palchecker("Race car"))
