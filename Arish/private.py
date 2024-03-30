class Base:
    __Name = None
    __Rollno = None
    __Grade = None
    def __init__(self,a,b,c):
        self.__Name = a
        self.__Rollno = b
        self.__Grade = c
    def access(self):
        return self.__Grade,self.__Name,self.__Rollno

    def display(self):
        print("Name:",self.__Name,"\nRollno:",self.__Rollno,"\nGrade:",self.__Grade)
A = Base("Arish","E22ITR005","O")
A.display()
print(list(A.access()))