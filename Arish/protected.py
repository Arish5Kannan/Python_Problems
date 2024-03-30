class Base:
    _Name =  None
    _Rollno = None
    _Dept = None
    def __init__(self,a,b,c):
        self._Name = a
        self._Rollno = b
        self._Dept = c
    def _display(self):
        print("Name:",self._Name,"\nRollno:",self._Rollno,"\nDept:",self._Dept)
class Derive(Base):
        def __init__(self,a,b,c):
            super().__init__(a,b,c)
        def Display(self):
            self._display()
A = Derive("Arish","E22ITR005","IT")
A.Display()
A._display()
b = Base("Ari","90","o")
b._display()
Base._display(b)