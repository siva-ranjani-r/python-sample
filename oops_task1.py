class student():
    def __init__(self, name, age,date,rollnumber):
        self.name=name
        self.age=age
        self.date=date
        self.rollnumber=rollnumber

    def mark(self):
        return self.name,self.age,self.date,self.rollnumber
        
name=str(input("Enter the name"))
age=int(input("Enter the age"))
date=int(input("Enter the date of birth"))
rollnumber=int(input("Enter the rollnumber"))

stu=student(name,age,date,rollnumber)
print(stu.mark())