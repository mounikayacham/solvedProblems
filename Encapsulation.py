'''class Student:
    def __init__(self):
        self.name='Mounika'
        self._marks=80
        self.__grade='A'
obj=Student()
print(obj.name,obj._marks)
print(obj._Student__grade)''' # output will genrate,but it is not reccommended to use

''''class Student:
    def __init__(self):
        self.__name=''
    def set_name(self,n):
        self.__name=n
    def get_name(self):
        return self.__name
obj=Student()
obj.set_name('mounika')
print('updated Name',obj.get_name())

class collage:
    def __init__(self,marks):
        self.__rollno=''
        self.__name=''
        self.__marks=0
    def set_details(self,name,rollno,marks):
        self.__name=name
        self.__rollno=rollno
        self.__marks=marks
    def get_details(self):
        return f'{self.__name}\n{self.__rollno}\nMarks is {self.__marks}'
c=collage(45)
c.set_details('mounika','22jn1a4528',45)
print(c.get_details())'''

class Employee:
    def __init__(self,emp_id,name,salary,dep):
        self.emp_id=emp_id#public
        self._dep=dep#protected
        self.__name=name#privated
        self.__salary=salary
    def set_salary(self,new_salary):
        if new_salary>0:
            self.__salary=new_salary
        else:
            print('Invalid')
    def get_salary(self):
        return self.__salary
    def set_name(self,name):
        if name.strip()!='':
            self.__name=name
        else:
            print('Error')
    def get_name(self):
        return self.__name
    def display(self):
        print(f" Public variable :{self.emp_id}\n protected: {self.__name}\n Privated :{self._dep}\n Protectd :Rs.{self.__salary}")
k=Employee('2342sd','mounika',2344,'ml')
k.display()
    

