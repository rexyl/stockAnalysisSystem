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

# def thread_starter(ind):
# 	mariadb_connection = mariadb.connect(host='52.34.22.14',port=3306,user='root', password='final_project',database='historical_stock')
# 	time_ = 0
# 	producer = KafkaProducer(bootstrap_servers='172.31.10.74:9092')
# 	sleep(2) 
# 	#to wait for kafka connection established
# 	#f = open('data/'+stocks[ind],'w+')
# 	cursor = mariadb_connection.cursor()
# 	prev_price = ''
# 	dif_cnt = 0
# 	while time_<5000:
# 		time_ = time_ + 1
# 		res = stock_quote(stocks[ind])
# 		if prev_price!=res[1]:
# 			try:
# 				uni_str = str2unixtime(res[0])
# 				producer.send('test', str(stocks[ind]+":"+uni_str+":"+res[1]))
# 				cmd_str = "INSERT INTO %s (UNICODE,PRICE) VALUES (%s,%s)" % (stocks[ind],uni_str,res[1])
# 				cursor.execute(cmd_str)
# 				prev_price = res[1]
# 				dif_cnt = dif_cnt + 1
# 				if dif_cnt==10:
# 					mariadb_connection.commit()
# 					dif_cnt = 0
# 			except:
# 				pass
# 			#f.write(res_str)
# 		time.sleep(2)
# 	mariadb_connection.close()
	#f.close()

# for i in range(0,len(stocks)):
# 	thread.start_new_thread(thread_starter,(i,))

# # for i in range(0,len(stocks)):
# # 	stock_quote(stocks[i])

# while 1:
# 	pass


