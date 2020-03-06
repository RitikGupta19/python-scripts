class Student:

	def __init__(self):
		self.name = "John"
		self.rollNumber = "183"
		self.age = "20"
		self.marks = "99"

	def Display(self):
		print("Name:",self.name)
		print("Roll number:",self.rollNumber)
		print("Age:",self.age)
		print("Marks:",self.marks)

	def setAge(self,age):
		self.age = age

	def setMarks(self,marks):
		self.marks = marks

stu1 = Student()
stu1.Display()
stu1.setMarks(100)
stu1.setAge(19)
stu1.Display()
