import requests,re
from bs4 import BeautifulSoup
from urllib.parse import quote
import time


def makingsoup():
	try:
		res=requests.get("http://www.nitp.ac.in/php/home.php")
	except: # If website is down or can't reach... it sleeps for 3 minutes and try's recursively
		time.sleep(300)
		makingsoup()
	return(BeautifulSoup(res.text,'lxml'))
	

# Announcement Section Tab
def announcements():
	soup=makingsoup()
	_div = soup.find('div', {'class':'ex1'})
	z= _div.find_all('a')
	return collection(z)
	
# It creates a list and add the title and links to the list
def collection(para):
	cool=[]
	for i in para:
		title= i.text
		link= i.get('href')
		if link[0]!='h':
			link='http://www.nitp.ac.in'+quote(link[2:])
		cool.append({'title':title,'link':link})
	cool.reverse()
	return cool

# Important Section Tab
def important():
	soup=makingsoup()
	_div1=soup.find('div',{'class':'ex2'})
	y=_div1.find_all('a')
	return collection(y)


def events():
	soup=makingsoup()
	_div2=soup.select('#opi')
	x=_div2[0].find_all('a')
	return collection(x)



def main():
	notice = announcements()
	notice1 = important()
	notice2=events()


	import pickle
	
# Dumping into the pickle file
	with open('ann_list', 'wb') as fp:
		pickle.dump(notice, fp)


	with open('imp_list','wb') as fp:
		pickle.dump(notice1,fp)
		
	with open('notice_list','wb') as fp:
		pickle.dump(notice2,fp)

# To reuse the stored data from a pickle file

	with open ('ann_list', 'rb') as fp:
		itemlist = pickle.load(fp)
	print(itemlist,len(itemlist))

	with open ('imp_list', 'rb') as fp:
		print(pickle.load(fp))
		
	with open ('notice_list','rb') as fp:
		print(pickle.load(fp))


if __name__ == '__main__':
	main()

