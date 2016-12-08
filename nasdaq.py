from time import sleep
from bs4 import BeautifulSoup
import urllib, time, os, re, csv,json,time,thread,datetime,time
import MySQLdb
import _config as cfg

#stock symbol for example:  ['BAC', 'C', 'IBM', 'AAPL', 'GE', 'T', 'MCD', 'NKE', 'TWTR', 'TSLA']
def get_time():
	return str(int(time.time()))

def stock_quote(stock):
	url = 'http://www.nasdaq.com/symbol/'+stock+'/real-time'
	html = urllib.urlopen(url)
	soup = BeautifulSoup(html,"html.parser")
	divs = soup.findAll('div',class_="qwidget-dollar",id = "qwidget_lastsale")
	time = soup.findAll('span',id = "qwidget_markettime")
	try:
		price = divs[0].get_text().replace('$','')
		time = time[0].get_text().encode('utf-8')
		return (time,price)
	except:
		return "Error time\n"


