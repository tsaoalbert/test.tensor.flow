
"""
(__sub__, __mul__, and __truediv__).
(__gt__, __ge__, __lt__, __le__, and __ne__)

"""
def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
     # xxx
     def __init__(self,a, b):
         if type(a)!= int or type(b)!= int :
            raise ValueError (" Have to be an integer " ) 
         if b==0:
            raise ValueError (" Denominator cannot be zero! " ) 

         if b < 0:
            a = -a; b = -b;
         
         g = gcd (a, b)
         self.num = a//g
         self.den =  b//g

     def __str__(self):
         return str(self.num)+"/"+str(self.den)

     def show(self):
         print(self.num,"/",self.den)

     def __add__(self,otherfraction):
         newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
         newden = self.den * otherfraction.den
         common = gcd(newnum,newden)
         return Fraction(newnum//common,newden//common)

     # xxx
     def __sub__(self, y):
         # x = a/b, y= c/d ==> x-y = (ad-bc)/bd
         a = self.num; b = self.den; c=y.num; d=y.den;
         return Fraction(a*d-b*c,b*d)

     def __eq__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum == secondnum

      # xxx
     def getNum (self):
        return self.num

      # xxx
     def getDen (self):
        return self.den

x = Fraction(2,3)
y = Fraction(1,2)
print(x-y)
print(x == y)
z = Fraction(1,0)

