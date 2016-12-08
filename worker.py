from time import sleep
from bs4 import BeautifulSoup
import urllib, time, os, re, csv,json,time,thread,datetime
import MySQLdb
import _config as cfg
from nasdaq import stock_quote,get_time
from analyser import analyser

def create_tables(symbol):
	mysql = MySQLdb.connect( host = cfg.HOST, user = cfg.USER, port = cfg.PORT, passwd = cfg.PASSWORD, db = cfg.DB )
	cursor = mysql.cursor()
	cmd_str = "CREATE TABLE IF NOT EXISTS %s (UNICODE varchar(15),PRICE float,PRIMARY KEY (UNICODE))" % (symbol)
	cursor.execute(cmd_str)
	cursor.execute('COMMIT')
	mysql.close()

def process(symbol,interval):
	mysql = MySQLdb.connect( host = cfg.HOST, user = cfg.USER, port = cfg.PORT, passwd = cfg.PASSWORD, db = cfg.DB )
	cursor = mysql.cursor()
	create_tables(symbol)
	time_ = 0
	symbol_analyser = analyser(symbol)
	sleep(2)

	prev_price = ''
	dif_cnt = 0
	while time_<cfg.max_iter:
		time_ = time_ + 1
		res = stock_quote(symbol)
		if prev_price!=res[1]:
			#try:
			uni_str = get_time()
			cmd_str = "INSERT INTO %s (UNICODE,PRICE) VALUES (%s,%s)" % (symbol,uni_str,res[1])
			symbol_analyser.add(float(res[1]), uni_str)
			cursor.execute(cmd_str)
			prev_price = res[1]
			dif_cnt = dif_cnt + 1
			if dif_cnt==10:
				cursor.execute('COMMIT')
				dif_cnt = 0
		time.sleep(interval)
	mysql.close()

process('AAPL', 2)
