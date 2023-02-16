#adding three varible
class myclass():
    x=5
add=myclass()
add1=myclass()
add2=myclass()
print(add.x+add1.x+add2.x)

#three object three attribute sum
class myclass():
    def __init__(self,a,b):
        self.firstvalue=a
        self.secondvalue=b
ob=myclass(3,4)
ob1=myclass(-2,4)
ob2=myclass(45,67)
print(ob.firstvalue+ob1.firstvalue+ob2.firstvalue)
print(ob.secondvalue+ob1.secondvalue+ob2.secondvalue)

#student datas
class student():
    def __init__(self, name, age,date,rollnumber):
        self.name=name
        self.age=age
        self.date=date
        self.rollnumber=rollnumber

    def __str__(self):
        return f"My name is:{self.name}, My age is {self.age}, My date of birth is:{self.date}, My rollnumber is:{self.rollnumber}"
        
name=str(input("Enter the name"))
age=int(input("Enter the age"))
date=int(input("Enter the date of birth"))
rollnumber=int(input("Enter the rollnumber"))

stu=student(name,age,date,rollnumber)
print(stu)