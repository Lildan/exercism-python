import math

class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, other):
        r = self.real + other.real
        i = self.imaginary + other.imaginary
        return ComplexNumber(r,i)

    def __mul__(self, other):
        r = self.real * other.real - self.imaginary * other.imaginary
        i = self.real * other.imaginary + other.real * self.imaginary
        return ComplexNumber(r,i)

    def __sub__(self, other):
        r = self.real - other.real
        i = self.imaginary - other.imaginary 
        return ComplexNumber(r,i)

    def __truediv__(self, other):
        div = other.real**2 + other.imaginary**2
        r = (self.real*other.real + self.imaginary*other.imaginary)/div
        i = (self.imaginary*other.real - self.real*other.imaginary)/div
        return ComplexNumber(r,i)

    def __abs__(self):
        return math.sqrt(self.real**2 + self.imaginary**2)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        r = math.exp(self.real)*math.cos(self.imaginary)
        i = math.exp(self.real)*math.sin(self.imaginary)

        if abs(r) < 0.00000001:
            r = 0
        if abs(i) < 0.00000001:
            i = 0

        return ComplexNumber(r,i)

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary