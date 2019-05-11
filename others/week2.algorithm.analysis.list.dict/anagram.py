#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__      = "Albert Tsao"
__copyright__   = "Copyright 2019"
"""
import itertools

def anagramSolution1(s1,s2):
    alist = list(s2)

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK



def anagramSolution2(s1,s2):
    """
    If s1 and s2 are sorted first, then they are anagram if s1==s2 

    @param param1: the 1st string
    @param param2: second string
    @return: true if s1 and s2 are anagram
    @raise keyError: raises an exception
    """

    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches

def anagramSolution3(s1,s2):
  for s3 in itertools.permutations(s1):
    if "".join(s3)==s2:
      return True
  return False

def anagramSolution4(s1,s2):
    """
      count and compare
    """
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True
    while j<26 and stillOK:
        if c1[j]==c2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK

def main():
  print(anagramSolution1('abcd','dcba'))
  print(anagramSolution2('abcde','edcba'))
  print(anagramSolution3('abcde','edcba'))
  print(anagramSolution4('apple','pleap'))
    # my code here

if __name__ == "__main__":
    main()

