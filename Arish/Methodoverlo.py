class Base:
    def pr(self,a=0,b=0,c=0):
        print(a+b+c)

A = Base()
A.pr(8,6)
A.pr(8,6,9)
A.pr(8)
A.pr()
