class Myclass:
	i = "hi there"
	def __init__(self):
		print "function #1 init"
	def f2(self):
		print "function #2"
	def f3(self):
			print "function #3"

myobj = Myclass()
myobj.f2()
myobj.f3()
print myobj.i
