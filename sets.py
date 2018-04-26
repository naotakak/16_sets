# AMatterBaby -- Shakil Rafi and Naotaka Kinoshita
# SoftDev2 pd7
# K16 -- Ready, set, math!
# 2018-04-26

def union(l1, l2):
    return l1 + [ x for x in l2 if x not in l1 ]

def intersection(l1, l2):
    return [ x for x in l1 if x in l2 ]

def set_difference(l1, l2):
    return [ x for x in l1 if x not in l2 ]

def symmetric_difference(l1, l2):
    return set_difference(l1, l2) + set_difference(l2, l1)

def cartesian_product(l1, l2):
    return [ (x, y) for x in l1 for y in l2 ]
