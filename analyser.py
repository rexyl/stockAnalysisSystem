import math
import datetime,time
import _config as cfg
from sns import send

class analyser(object):
	"""docstring for analyser"""
	symbol = ''
	avg = 0
	avg_square = 0
	n = 0
	avg_xy = 0
	avg_time_square = 0

	def __init__(self, symbol):
		self.symbol = symbol

	def add(self,x, time):
		int_time = int(time)
		if self.avg != 0:
			self.check_alart(x,cfg.default_multiplier, time)
		self.avg = self.avg * (self.n/(self.n+1.0)) + x/(self.n+1.0)
		self.avg_square = self.avg_square * (self.n/(self.n+1.0)) + x*x/(self.n+1.0)
		self.avg_xy = self.avg_xy * (self.n/(self.n+1.0)) + x*int_time/(self.n+1.0)
		self.avg_time_square = self.avg_time_square * (self.n/(self.n+1.0)) + int_time*int_time/(self.n+1.0)
		self.n += 1

	def getDev(self):
		return math.sqrt(self.avg_square - self.avg*self.avg)

	def getAvg(self):
		return self.avg

	def check_alart(self, x, devMultiplier, time_):
		readable = datetime.datetime.fromtimestamp(int(time_)).strftime('%Y-%m-%d %H:%M:%S')
		if x > self.getAvg() + devMultiplier*self.getDev():
			send( "Symbol {}({}) exceed average {} by {} deviation at time {}, {}\nAccording to our prediction, next trading price will be around {}".format(self.symbol,x,self.avg, devMultiplier, time_, readable, self.apprioximate_by_time(int(time.time()))))
		if x < self.getAvg() - devMultiplier*self.getDev():
			send( "Symbol {}({}) below average {} by {} deviation at time {}, {}\nAccording to our prediction, next trading price will be around {}".format(self.symbol,x,self.avg, devMultiplier, time_, readable, self.apprioximate_by_time(int(time.time()))))

	def apprioximate_by_time(self, time):
		#least square approximate
		if self.n < 5:
			print('Too few data point, cannot do a reasonable regression')
			return 0.0
		beta = self.avg_xy/self.avg_time_square
		return time*beta

# t = analyser('AAPL')
# t.add(100.0,str(int(time.time())))
# time.sleep(1)
# t.add(110.0,str(int(time.time())))
# time.sleep(1)
# t.add(120.0,str(int(time.time())))
# time.sleep(1)
# t.add(90.0,str(int(time.time())))
# time.sleep(1)
# t.add(95.0,str(int(time.time())))
# time.sleep(1)
# t.add(80.0,str(int(time.time())))
# time.sleep(1)
# t.add(115.0,str(int(time.time())))
# time.sleep(1)
# t.add(120.0,str(int(time.time())))
# time.sleep(1)
# t.apprioximate_by_time(int(time.time()))

