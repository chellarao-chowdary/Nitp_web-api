# Coded by Chellarao Chowdary on 25th Oct 2020

import requests
from bs4 import BeautifulSoup
from urllib.parse import quote


def getNews(category):
	"""
	** Fetch requeired category **
	"""
	newsDictionary={
		'success':True,
		'category':category,
		'data':[]
	}
	print(category)
	card = category in ['all','announcements','important','events','blink','archive']
	if not card:
		newsDictionary['success'] = False
		newsDictionary['error'] = 'Invalid Category'
		return newsDictionary

	try:
		if category!="archive":
			htmlBody=requests.get("http://www.nitp.ac.in/php/home.php")
			# with open("index.html",encoding="utf8") as fp:
			# 	soup = BeautifulSoup(fp,'lxml')
		else:
			htmlBody=requests.get("http://www.nitp.ac.in/php/archivedNotices.php")
			# with open("archive.html",encoding="utf8") as fp:
			# 	soup = BeautifulSoup(fp,'lxml')

	except Exception as e:
		newsDictionary['success']=False
		if hasattr(e, 'message'):
			e = e.message
		newsDictionary['error']=str(e)
		return newsDictionary

	soup = BeautifulSoup(htmlBody.text, 'lxml')
	if category=='all':	
		_,notice = announcements(soup)
		_,notice1 = important(soup)
		_,notice2 = events(soup)
		_,notice3 = blink(soup)
		newsDictionary['data'].append({'announcements':notice,'important':notice1,'events':notice2,'blink':notice3})
		newsDictionary['total'] = len(notice) + len(notice1) + len(notice2) + len(notice3)
		return newsDictionary

	if category=='announcements':
		res,notice = announcements(soup)
	elif category=='important':
		res,notice = important(soup)
	elif category=='events':
		res,notice = events(soup)
	elif category=='blink':
		res,notice = blink(soup)
	elif category=='archive':
		res,notice=important(soup)

	if not res:
		newsDictionary['success']=False
		newsDictionary['error']=notice
		return newsDictionary
		
	newsDictionary['data'] = notice
	newsDictionary['total']= len(notice)
	return newsDictionary



# Announcement Section Tab
def announcements(soup):
	"""
	** Announcements Tab**
	"""
	try:
		_div = soup.find('div', {'class':'ex1'})
		z= _div.find_all('a')
		return True,collection(z)
	except Exception as e:
		return False,[str(e)]
# It creates a list and add the title and links to the list
def collection(para):
	"""
	** Convet data to list **
	"""
	cool=[]
	for i in para:
		title= i.text
		link= i.get('href')
		if link and link[0]!='h':
			link='http://www.nitp.ac.in'+quote(link[2:])
		if title or link:
			cool.append({'title':title,'link':link})
	return cool

# Important Section Tab
def important(soup):
	"""
	** Important Tab **
	"""
	try:
		_div1=soup.find('div',{'class':'ex2'})
		y=_div1.find_all('a')
		return True,collection(y)
	except Exception as e:
		return False,[str(e)]


def events(soup):
	"""
	** Events Tab **
	"""
	try:	
		_div2=soup.select('#opi')
		x=_div2[0].find_all('a')
		return True,collection(x)
	except Exception as e:
		return False,[str(e)]
def blink(soup):
	"""
	** Blink notices **
	"""
	_div3=soup.select('.blinking') or soup.select('.blinking3')
	if len(_div3)!=0:
		cool1=[]
		for i in _div3:
			title= i.text
			try:
				link = i.a.get('href')
			except:
				link='http://www.nitp.ac.in'
			if link and link[0]!='h':
				link='http://www.nitp.ac.in'+ quote(link[2:])
			cool1.append({'title':title,'link':link})
		cool1.reverse()
		return True,cool1
	return False,['No data Available']

