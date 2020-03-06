class Circle:
	radius = 10

	def __init__(self):
		self.radius = 20

	def getArea(self,radius):
		self.area = 3.14 * radius * radius

	def getCircumfrence(self,radius):
		self.circum = 2 * 3.14 * radius

c = Circle()
c.getArea(10)
print("Area:",c.area)
c.getCircumfrence(10)
print("Circumfrence:",c.circum)