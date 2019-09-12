"""Funtion that takes a list of integers and return the sum of the negative integers in the list
"""
def sumNegativeInts(listInt):
    m = 0
    for x in listInt:
        if x < 0:
            m+=x
    return(int(m))
#2 variant
def sum_of_neg(a):
  return sum(x for x in a if x<0)