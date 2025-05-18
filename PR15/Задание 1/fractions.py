from math import gcd


class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        g = gcd(numerator, denominator)
        self.numerator = numerator // g
        self.denominator = denominator // g
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def multiply(self, other):
        new_num = self.numerator * other.numerator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def divide(self, other):
        if other.numerator == 0:
            raise ValueError("Division by zero")
        new_num = self.numerator * other.denominator
        new_den = self.denominator * other.numerator
        return Fraction(new_num, new_den)


def multiply_fractions(fractions_list):
    if not fractions_list:
        return Fraction(1, 1)
    result = fractions_list[0]
    for frac in fractions_list[1:]:
        result = result.multiply(frac)
    return result
