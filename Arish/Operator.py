class Base:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __add__(self,other):
        print(self.a+other.b)
A = Base(4,6)
B = Base(4,9)
print(A+B)