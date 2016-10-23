# Data Structures Ch. 1-13
# Fraction Class

def gcd(m,n): #Euclid's Algorithm to find greatest common divisor
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn        #second number becomes first value
        n = oldm%oldn   #remainder becomes second value for next loop
    return n

class Fraction:
    # Constructor
    def __init__(self,top,bottom): #constructor always has self parameter
        self.num = top
        self.den = bottom
    def show(self): #normal print(frac) won't work at first.
        print self.num,'/',self.den #This is an overloaded method telling class how to print
    def __str__(self):  #overloaded string method to convert to string used by print
        return str(self.num)+"/"+str(self.den) #print will now work
    def __add__(self, other):   #overload the '+' operator
        numResult = self.num*other.den + self.den*other.num
        denResult = self.den * other.den
        commonDivisor = gcd(numResult,denResult) #to find lowest common denom
        return Fraction(numResult//commonDivisor,denResult//commonDivisor) #result of adding two fractions
    def __eq__(self, other):    #overloaded equality operator
        firstVal = self.num * other.den
        secondVal = other.num * self.den
        return firstVal == secondVal
    def __mul__(self, other):
        numResult = self.num * other.num
        denResult = self.den * other.den
        commonDivisor = gcd(numResult,denResult) #to find lowest common denom
        return Fraction(numResult//commonDivisor,denResult//commonDivisor)
    def __div__(self, other):
        numResult = self.num * other.den
        denResult = self.den * other.num
        commonDivisor = gcd(numResult,denResult) #to find lowest common denom
        return Fraction(numResult//commonDivisor,denResult//commonDivisor)
    def __sub__(self, other):
        numResult = self.num * other.den - other.num * self.den
        denResult = self.den * other.den
        commonDivisor = gcd(numResult,denResult) #to find lowest common denom
        return Fraction(numResult//commonDivisor, denResult//commonDivisor)
    def __lt__(self, other):
        firstNum = self.num * other.den
        secondNum = other.num * self.den
        return firstNum < secondNum
    def __gt__(self, other):
        firstNum = self.num * other.den
        secondNum = other.num * self.den
        return firstNum > secondNum


# myFraction = Fraction(3,5)
# myFraction.show()
# print(myFraction)
f1 = Fraction(1,3)
f2 = Fraction(1,5)
print(f1+f2)
print(f1*f2)
print(f1==f2)
print(f1/f2)
print(f1-f2)
print(f1<f2)
print(f1>f2)