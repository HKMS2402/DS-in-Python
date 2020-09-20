#Naive Approach
#Not Optimized Approach
class GCD:
    def __init__(self):
        self.__gcd = 0

    def factors(self,x):
        factors = []
        for i in range(1,x+1):
            if(x%i) == 0:
                factors.append(i)
        return factors        

    def naiveGCDv1(self,m,n):
        fm = self.factors(m)
        fn = self.factors(n)
        cf = []
        for i in fm:
            if i in fn:
                cf.append(i)
        return cf[-1]

    def naiveGCDv2(self,m,n):
        num = max(m,n)
        cf = []
        for i in range(1,num+1):
            if(n%i ==0) and (m%i ==0):
                cf.append(i)
        return cf[-1]

    def naiveGCDv3(self,m,n):
        num = min(m,n)
        cf = []
        for i in range(1,num+1):
            if(n%i ==0) and (m%i ==0):
                cf.append(i)
        return cf[-1]

        

x = GCD()
print(x.naiveGCDv2(14,63))