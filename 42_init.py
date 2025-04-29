class computer:     #class

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def confing(self):
        print("config is=",self.cpu,self.ram)

com1 = computer('i7',16)       #object
com1.confing()


# 👉Student:

class student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def students(self):
        print("Name is=",self.name,"Marks is=",self.marks)

s1 = student("Twinkal",90)
s1.students()