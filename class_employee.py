#usr/bin/python

class employee:

        def __init__(self, name, salary):
                self.name = name
                self.salary = salary
       
	def displayEmployee(self):

                print "Name : ", self.name,  ", Salary: ", self.salary

emp1 = employee("Galit", 1000)
emp2 = employee("Yossi", 5000)
employee.displayEmployee(emp1)
employee.displayEmployee(emp2)
