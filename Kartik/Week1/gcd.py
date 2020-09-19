#Naive Approach
class naiveGCD:
    def __init__(self):
        self.__gcd = 0

    def factors(self,x):
        factors = []
        for i in range(1,x+1):
            if(x%i) == 0:
                factors.append(i)
        return factors        

    def gcd(self,m,n):
        fm = self.factors(m)
        fn = self.factors(n)
        cf = []
        for i in fm:
            if i in fn:
                cf.append(i)
        return cf[-1]

x = naiveGCD()
print(x.gcd(14,63))