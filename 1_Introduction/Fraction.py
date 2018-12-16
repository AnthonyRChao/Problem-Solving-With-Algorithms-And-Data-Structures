"""
Fraction Class
"""


class Fraction:
    """An implementation of a Fraction class."""

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, frac):
        common_div = self.gcd(self.den, frac.den)
        num_new = ((self.num * frac.den) + (frac.num * self.den)) // common_div
        den_new = (self.den * frac.den) // common_div
        return str(num_new) + "/" + str(den_new)

    def __eq__(self, frac):
        num_self = self.num * frac.den
        num_frac = frac.num * self.den
        return num_self == num_frac

    def __mult__(self, frac):
        common_div = self.gcd(self.den, frac.den)
        num_new = self.num * frac.num
        den_new = self.den * frac.den
        return Fraction(num_new, den_new)

    def __div__(self, frac):
        num_new = self.num * frac.den
        den_new = self.den * frac.num
        return Fraction(num_new, den_new)

    def __sub__(self, frac):
        pass

    def __lt__(self, frac):
        pass

    def __gt__(self, frac):
        pass

    def gcd(self, m, n):
        """The best algorithm to find the GCD is Euclid's Algorithm.

        Euclid’s Algorithm states that the greatest common divisor of two
        integers m and n is n if n divides m evenly. However, if n does
        not divide m evenly, then the answer is the greatest common
        divisor of n and the remainder of m divided by n. Note that
        this implementation of the GCD algorithm only works when the
        denominator is positive. This is acceptable for our fraction
        class because we have said that a negative fraction will be
        represented by a negative numerator.
        """
        while m % n != 0:
            m_old = m
            n_old = n

            m = n_old
            n = m_old % n_old

        return n


if __name__ == '__main__':

    f1 = Fraction(1, 2)
    f2 = Fraction(1, 4)
    print(f1.__div__(f2))

    f3 = Fraction(3, 2)
    f4 = Fraction(7, 8)
    print(f3.__div__(f4))
