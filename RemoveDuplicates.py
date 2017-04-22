
text_file = open("Product_Titles.txt", "r+")

print("Removing duplicates...")
u = text_file.read()
d = u.split("\n")

unique_list = []
for x in d:
	if x is not None and x not in unique_list:
		print(x)
		y = x.replace("&amp;", "&")
		y = y.replace("&reg;", "")
		y = y.replace("&quot;", "\"")
		print(y)
		unique_list.append(y)

text_file.seek(0)
text_file.truncate()

text_file.write("\n".join(unique_list))

text_file.close()
