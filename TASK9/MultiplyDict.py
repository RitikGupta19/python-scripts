dict1 = {'one' : 1, 'two' : 2 , 'three' : 3, 'four' : 4}
mul = 1
for (key,value) in dict1.items():
	mul = mul * value
print(mul)