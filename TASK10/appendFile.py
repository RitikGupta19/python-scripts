with open("file.txt","a",encoding="utf-8") as f:
	f.write("\nPython is intresting.")

with open("file.txt","r",encoding="utf-8") as f:
	print(f.read())
