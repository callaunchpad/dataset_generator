import json
import os
import requests

from bs4 import BeautifulSoup

# header = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) " +
# 				"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 " + 
# 				"Safari/537.36"}
# soup = BeautifulSoup(urllib2.urlopen(urllib2.Request("https://www.google.co.in/search?q=hat&source=lnms&tbm=isch",headers=header)),'html.parser')

# print(soup)
# exit()

text_file = open("Product_Titles.txt", "r")
list_of_items = text_file.read().split('\n')
# list_of_items = ["hat"]
text_file.close()

limit = 20

def getSoup(url, header):
	return BeautifulSoup(requests.get(url, headers=header).content,
		'html.parser')

print("~Entering loop...")

for image_type in list_of_items:
	counter = 0

	query = image_type
	query = query.split(" ")
	query = '+'.join(query)
	url = ["https://www.google.co.in/search?q=" + query + "&source=lnms&tbm=" +
			"isch"][0]

	print("~URL set...")
	print(url)

	DIR = "Image_Data"
	header = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) " +
				"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 " + 
				"Safari/537.36"}
	soup = getSoup(url, header)

	actual_images = [] # contains the link for large original images, type of image
	for a in soup.find_all("div", class_="rg_meta"):
		link, Type = json.loads(a.text)["ou"], json.loads(a.text)["ity"]

		actual_images.append((link, Type))

	print("There are a total of " + str(len(actual_images)) + " images.")

	if not os.path.exists(DIR):
		os.mkdir(DIR)

	DIR = DIR + "/" + image_type

	if not os.path.exists(DIR):
		os.mkdir(DIR)

	print("~Now searching for {" + image_type + "}...")

	# print images
	for i, (img, Type) in enumerate(actual_images):

		if counter >= limit:
			break

		try:
			req = requests.get(img, headers={'User-Agent': str(header)})
			raw_img = req.content

			cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
			print(cntr)

			if len(Type) == 0:
				f = open(os.path.join(DIR, image_type + "_" + str(cntr) + ".jpg"),
					'wb')
			else:
				f = open(os.path.join(DIR, image_type + "_" + str(cntr) + "." +
					Type), 'wb')

			f.write(raw_img)
			f.close()

		except Exception as e:
			print("Could not load: " + img + ".")
			print(e)

		counter += 1

print("---Finished scraping---")
