# -*- coding: utf-8 -*-
import urllib
import mechanize
from bs4 import BeautifulSoup
import re

from tutorinteligente.models import *

from google import search

class Dominio:

	def acao(self, percepcao, pergunta, nivel_objeto_ensino):
		if percepcao == 'enviar_objeto_ensino':
			return self.procurar_objeto_ensino(pergunta, nivel_objeto_ensino)


	def procurar_objeto_ensino(self, pergunta, nivel_objeto_ensino):
		objeto_ensino = Objeto_Ensino.objects.filter(tags__search = pergunta, nivel = nivel_objeto_ensino)
		#print dir(objeto_ensino[0])
		#objeto_ensino = nivel_objeto_ensino
		if not objeto_ensino:
			objeto_ensino = self.googleSearch(pergunta)
			#print dir(objeto_ensino)

		return objeto_ensino


	#def googleSearch(self, link, depth):
	def googleSearch(self, link):
		results_array = []
		for url in search(link + "wiki", tld='com.br', lang='pt', stop=1):
			results_array = url

		return results_array
		# br = mechanize.Browser()
		# br.set_handle_robots(False)
		# br.addheaders = [('User-agent','chrome')]

		# term = link.replace(" ","+")
		# #query = "http://www.google.com.br/search?num=1&q="+term+"&start="+depth
		# #query = "http://www.google.com.br/search?q="+term+"&start="+depth
		# query = "http://www.google.com.br/search?q="+term+"%20wiki"+"&oq="+term+"%20wiki"
		# htmltext = br.open(query).read()
		# soup = BeautifulSoup(htmltext)
		# search = soup.findAll('div',attrs={'id':'search'})
		# searchtext = str(search[0])
		# soup1 = BeautifulSoup(searchtext)
		# list_items = soup1.findAll('li')
		# regex = "q(?!.*q).*?&amp"
		# pattern = re.compile(regex)

		# results_array = []

		# for li in  list_items:
		# 	soup2 = BeautifulSoup(str(li))
		# 	links = soup2.findAll('a')
		# 	source_link = links[0]
		# 	source_url = re.findall(pattern,str(source_link))
		# 	if len(source_url)>0:
		# 		results_array.append(str(source_url[0].replace("q=","").replace("&amp","")))
		# #results_array = [1,2,3]

		# return results_array

		#print gSearch("python","0")