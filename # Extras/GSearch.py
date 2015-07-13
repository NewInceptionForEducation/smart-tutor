import urllib
import mechanize
from bs4 import BeautifulSoup
import re

def getGoogleLinks(link,depth):
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.addheaders = [('User-agent','chrome')]

	term = link.replace(" ","+")
	#query = "http://www.google.com.br/search?num=100&q="+term+"&start="+depth
	query = "http://www.google.com.br/search?q="+term+"&start="+depth
	htmltext = br.open(query).read()
	soup = BeautifulSoup(htmltext)
	search = soup.findAll('div',attrs={'id':'search'})
	searchtext = str(search[0])
	soup1 = BeautifulSoup(searchtext)
	list_items = soup1.findAll('li')
	regex = "q(?!.*q).*?&amp"
	pattern = re.compile(regex)

	results_array = []

	for li in  list_items:
		soup2 = BeautifulSoup(str(li))
		links = soup2.findAll('a')
		source_link = links[0]
		source_url = re.findall(pattern,str(source_link))
		if len(source_url)>0:
			results_array.append(str(source_url[0].replace("q=","").replace("&amp","")))
	#results_array = [1,2,3]
	
	return results_array


print getGoogleLinks("python","0")