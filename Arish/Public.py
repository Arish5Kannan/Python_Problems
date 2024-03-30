class Base:
    A = None
    B = None
    def __init__(self,a,b):
        #Public variables accessing
        self.A = a
        self.B = b
    def Add(self):
        return self.A+self.B
C = Base(3,5)
s = C.Add()
print("SUM :",s)


