with open("file.txt","r",encoding="utf-8") as f:
	lines = f.readlines()
	print(len(lines))