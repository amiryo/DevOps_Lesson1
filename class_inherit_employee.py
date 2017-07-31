#usr/bin/python

class employee:

        def __init__(self, name, salary):
                self.name = name
                self.salary = salary

        def displayEmployee(self):

                return "Name : " + self.name +  ", Salary: " + self.salary


class person(employee):

    def __init__(self, name, salary, staffnum):
        employee.__init__(self,name,salary)
        self.staffnum = staffnum

    def GetEmployee(self):
        return employee.displayEmployee(self) + ", " +  "number: " + self.staffnum



emp1 = employee("Galit", "1000")
print(employee.displayEmployee(emp1))
#emp2 = employee("Yossi", "5000")
#employee.displayEmployee(emp1)
#employee.displayEmployee(emp2)
stuf = person("amir","2000","10")
print(stuf.GetEmployee())
