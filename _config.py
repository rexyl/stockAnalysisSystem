import MySQLdb

HOST = 'stockdb.c5omltdabdic.us-east-1.rds.amazonaws.com'
PORT = 3306
USER = 'root'
PASSWORD = 'ngnfinal'
DB = 'stockDB'
mysql = MySQLdb.connect( host = HOST, user = USER, port = PORT, passwd = PASSWORD, db = DB )
bootstrap_servers = "172.31.10.74:9092"
max_iter = 1000
default_multiplier = 3


AccessKeyID = 'AKIAIM3UOGIUW3AXRGLQ'
SecretAccessKey = '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'

