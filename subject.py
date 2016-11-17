from abc import ABCMeta, abstractmethod


class Subject(object):
	def __init__(self, name, datas=[]):
		self.name = name
		self.datas = datas
	
	def __convert_encode(self):
		for i in range(len(self.datas)):
			if isinstance(self.datas[i], unicode):
				self.datas[i] = self.datas[i].encode("utf-8")
	
	def convert_unit(self):
		self.__convert_encode()


class DateSubject(Subject):
	def __init__(self, name, datas=[]):
		super(DateSubject, self).__init__(name, datas)
	
	def convert_unit(self):
		super(DateSubject, self).convert_unit()


class MoneySubject(Subject):
	def __init__(self, name, datas=[]):
		super(MoneySubject, self).__init__(name, datas)
	
	def convert_unit(self):
		super(MoneySubject, self).convert_unit()
		for i in range(len(self.datas)):
			if str(self.datas[i]) == "":
				self.datas[i] = 0
			else:
				self.datas[i] = round(self.datas[i] / 10000, 3)
