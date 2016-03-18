"""
File: Histogram2.py

Copyright (c) 2016 Lauren Graziani

License: MIT
"""
def bar(n):
    st= ""
    for i in range(n+1):
        st += "*"
    print "%2d | %s " %  (i, st)

def histogram(title, mylist):
    print " n | Data"
    print "---+------------------"
    for i in mylist:
        bar(i)

histogram("Data", [4, 9, 13, 5])
