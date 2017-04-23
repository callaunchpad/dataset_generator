import ast
import gzip
import multiprocessing

from joblib import Parallel, delayed


rank = 250
num_cores = multiprocessing.cpu_count()
eval_func = ast.literal_eval

def validate(d):
	if any(value < rank for value in d.values()):
		return True
	return False

text_file = open("Product_Titles.txt", "w")
key1 = 'title'
key2 = 'salesRank'

with gzip.open("metadata.json.gz", "rb") as f:
	print("Unzipping metadata...")
	u = f.read().decode("ascii")
	print("Dumping...")
	d = u.split("\n")
	# d = [ast.literal_eval(s) for s in d if s]
	d = Parallel(n_jobs=num_cores)(delayed(eval_func)(ss) for ss in s if ss)
	print("Eval done! Writing to file...")
	for i in d:
		print(i)
		if key1 in i and key2 in i and validate(i[key2]):
			try:
				w = i[key1] + ""
				text_file.write(w + "\n")
			except e:
				continue

text_file.close()
