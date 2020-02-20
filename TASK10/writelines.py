with open("file.txt", "a", encoding = "utf-8")as f:
	lines = ["\nI am doing engineering", "\nIt is a 4 yr course", "\nEngineers can do everything!!"]
	f.writelines(lines)


