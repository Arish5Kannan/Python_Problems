class Base:
    def pr(self):
        print("Base class")
class Derive(Base):
    def pr(self):
        print("Derived class")
A = Derive()
Derive.pr(A)
Derive.pr(A)
