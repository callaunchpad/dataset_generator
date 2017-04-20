import gzip


text_file = open("Product_Titles.txt", "w")
key1 = 'title'
key2 = ''

with gzip.open("metadata.json.gz", "rb") as f:
		print("Unzipping metadata...")
		u = f.read().decode("ascii")
		print("Dumping...")
		d = u.split("\n")
		for i in d:
			if key1 in i and key2 in i and:
				try:
					w = eval(i)[key] + ""
					text_file.write(w + "\n")
				except e:
					continue

text_file.close()