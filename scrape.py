import mechanize
from bs4 import BeautifulSoup

link = "http://xkcd.com/"

br = mechanize.Browser()

for i in range (90,1380): 
	print ("Opening",i)
	response = br.open(link+str(i))
	html = response.read()
	soup = BeautifulSoup(html)
	img = soup.find_all('img')
	src = img[2].get('src')
	title = img[2].get('title')
	print type(title)
	#title = str(title)
	response = br.open(src)
	html = response.read()
	fp = open(title,'w+')
	fp.write(html)
	fp.close()

