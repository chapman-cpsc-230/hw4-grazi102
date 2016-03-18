"""
Name file: Histogram.py

### Length of an integer

Define a function `digits(n)` that calculates the number of digits
(plus the sign for negative numbers) in an integer.
For example `digits(521)` should return `3`; `digits(-4530)` should return `5`.

Name file: digits.py
"""
def digits(string):
    print "length of string:", len(str(string))
def test_digits():
    digits(-12345)
test_digits()
