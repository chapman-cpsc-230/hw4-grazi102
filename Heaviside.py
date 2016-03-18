"""
File: Heaviside.py

Copyright (c) 2016 Lauren Graziani

License: MIT

Excersice 3.23 from book.
"""



def H(x): #Write formula
    if x < 0:
        value = 0
    else:
        value = 1
    return value

def test_H():
    if H(-10)!=0:
        print "Error"
    else:
        print "H(-10)=", H(-10)
    if H(-10**-15)!=0:
        print "Error"
    else:
        print "H(-10**-15)=", H(-10**-15)
    if H(0)!=1:
        print "Error"
    else:
        print "H(0)=", H(0)
    if H(10**-15)!= 1:
        print "Error"
    else:
        print "H(10**-15)=", H(10**-15)
    if H(10)!=1:
        print "Error"
    else:
        print "H(10)=", H(10)
test_H()
