list1 = [1,2,2,3,3,3,4,4,4,4,5,6,7,7]
set1 = set(list1)
print (set1)
num = int(input("Enter number of item to remove : "))
while(num):
	set1.pop()
	num = num - 1
print (set1)

