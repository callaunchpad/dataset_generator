
text_file = open("Product_Titles.txt", "r+")

print("Removing duplicates...")
u = text_file.read()
d = u.split("\n")

unique_list = []
for x in d:
	if x is not None and x not in unique_list:
		print(x)
		unique_list.append(x)

text_file.seek(0)
text_file.truncate()

text_file.write("\n".join(unique_list))

text_file.close()
