"""
File: smoothed_Heaviside.py

Copyright (c) 2016 Lauren Graziani

License: MIT

Excercise 3.24 from book
"""
#a
from math import pi, sin
def H_eps(x,eps=0.01):
    if x < -eps:
        result = 0 #do case (1)
    elif  x <= eps:  #else if
        x_over_eps= x/eps
        result = (0.5*(1.0+x_over_eps+ sin(pi*(x_over_eps))/pi))#do case (2)
    else:  #Don't need to put x>e cuz its infered from line 11
        result = 1 #do case (3)
    return result
def test_H_eps():

        print "H_eps(-10)=", H_eps(-10)

        print "H_eps(-10**-3)=", H_eps(-10**-3)

        print "H_eps(0)=", H_eps(0)

        print "H_eps(10**-3)=", H_eps(10**-3)

        print "H_eps(10)=", H_eps(10)

test_H_eps()
