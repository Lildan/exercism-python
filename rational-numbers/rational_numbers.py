from __future__ import division

def GDC(a,b):
    if b == 0:
        return a
    return GDC(b, a%b)

class Rational(object):
    def __init__(self, numer, denom):
        d = GDC(numer,denom)
        self.numer = numer/d
        self.denom = denom/d

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        a = self.numer * other.denom + other.numer * self.denom
        b = self.denom * other.denom

        return Rational(a,b)

    def __sub__(self, other):
        a = self.numer * other.denom - other.numer * self.denom
        b = self.denom * other.denom

        return Rational(a,b)

    def __mul__(self, other):
        return Rational(self.numer*other.numer, self.denom*other.denom)

    def __truediv__(self, other):
        a = self.numer*other.denom
        b = self.denom*other.numer

        return Rational(a, b)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        a = self.numer**power
        b = self.denom**power

        return Rational(a, b)

    def __rpow__(self, base):
        return pow(base**self.numer,1./self.denom)