n = int(input("Enter no. of lines to read : "))
with open("file.txt","r",encoding="utf-8") as f:
	for i in range(n):
		line = f.readline()
		print(line)
