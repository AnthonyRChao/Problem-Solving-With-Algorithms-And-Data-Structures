# What is Shallow / Deep Equality?

Shallow Equality: occurs when two references point to the same object.

For example(without Fraction.__eq__() implemented):

>>> f1 = Fraction(1,2)
>>> f2 = f1
>>> f1 == f2
>>> True

>>> f3 = Fraction(1,3)
>>> f1 == f3
>>> False

Deep Equality: equality based on the same *value* rather than same reference,
by overriding the __eq__() method. The __eq__() method compares the values
of two objects and returns `True` if their values are the same, and `False`
otherwise.
