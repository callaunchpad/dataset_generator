import gzip


text_file = open("Product_Titles.txt", "w")
key = 'title'

with gzip.open("metadata.json.gz", "rb") as f:
		print("Unzipping metadata...")
		u = f.read().decode("ascii")
		print("Dumping...")
		d = u.split("\n")
		for i in d:
			if key in i:
				try:
					w = eval(i)[key] + ""
					text_file.write(w + "\n")
				except e:
					continue

text_file.close()