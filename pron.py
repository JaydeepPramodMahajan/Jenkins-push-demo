class A:
    total_count=0
    def __init__(self,name) :
        self.__name=name
        A.total_count=A.total_count+1
    @classmethod
    def count_ret(cls):
        return cls.total_count
    
p1=A("Sujay")
p2=A("Rashmi")
print(p1.count_ret())
print(p2.count_ret())
@classmethod
def external_fun(cls):
    def __str__(cls):
        return "String "

A.external_function=classmethod(external_fun)
print(p1.external_function())

del A.external_function
import time
class time_exe():
    def __init__(self,func):
        self.func=func
    def __call__(self):
        print("Say my name.......")
        self.func()
        print("You are God Damn right....")
        
@time_exe
def func():
    print("You are Heiunsenberg!!")
func()
    
class private_acess:
    def __init__(self,name) -> None:
        self.__name=name
    @property
    def print_var(self):
        return self.__name
    @print_var.setter
    def set_val(self,name):
        self.__name=name


p1=private_acess("Jay")
print(p1.print_var)
p1.set_val="Deep"
print(p1.print_var)


