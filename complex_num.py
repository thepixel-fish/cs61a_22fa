class Number:
    def __add__(self, other):
        return self.add(other)
    def __mul__(self, other):
        return self.mult(other)

class Complex(Number): 
    def add(self, other):
        return ComplexRI(self.real + other.real, self.imag + other.imag)
    def mult(self, other):
        return ComplexMA(self.magnitude * other.magnitude, self.angle + other.angle)
    def __repr__(self):
        return self.__repr__()

from math import atan2, sqrt
class ComplexRI(Complex):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    @property
    def magnitude(self):
        return sqrt(self.real ** 2 + self.imag)
    @property
    def angle(self):
        return atan2(self.real, self.imag)
    def __repr__(self):
        return 'ComplexRI({0:g}, {1:g})'.format(self.real, self.imag)
    def __str__(self):
        return f'{self.real}+{self.imag}i'    
from math import cos, sin, pi
class ComplexMA(Complex):
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle

    @property
    def real(self):
        return self.magnitude * cos(self.angle)
    
    @property
    def imag(self):
        return self.magnitude * sin(self.angle)
    def __repr__(self):
        return 'ComplexMA({0:g}, {1:g} * pi)'.format(self.magnitude, self.angle / pi)