class person:
    def set(self,name,age):
        self.name = name
        self.age = age 
class Student (person):
    course = 1 
dima = Student ()
dima.set("Dima",16)
print(dima.name,"\n",dima.age,"\n",dima.course,"\n")

class Teacher (person):
    salary = 12000
victoria = Teacher ()
victoria.set("Victoria",33)
print(victoria.name,'\n',victoria.age,'\n',victoria.salary)