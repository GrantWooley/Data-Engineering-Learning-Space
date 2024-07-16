# -*- coding: utf-8 -*-
"""
File used for going through courses, learning material, questions, etc...
"""

# This is the file ill be using for working on list comprehension today.


#Working on the hack rank list copmrehension problem now.
#[itemtoadd for item in iterable if condition ==True ]

# i can be between 0 and x
#is random user input.

"""
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    """

x = 1
y = 1
z = 2
n = 3

# Exvar = [x  for x in range(0,10) if x ,5]
#Allpermutations = [[i,j,k] for [i,j,k] in range(0,10) if i+j+k != n ]

AcceptablePermutations = [[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k != n]
AcceptablePermutations.sort()
print(AcceptablePermutations)