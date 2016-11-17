# coding: utf-8
from xlwt import *


class SharesAnalysis:
	work_book = None
	sheet = None
	
	def __init__(self, subjects=[], rates=[]):
		self.subjects = subjects
		self.rates = rates
		for i in range(len(rates)):
			rates[i].calculate()
		self.__create_analysis_sheet()
		self.__write()
	
	def __create_analysis_sheet(self):
		self.work_book = Workbook()
		self.sheet = self.work_book.add_sheet("sheet1", cell_overwrite_ok=True)
		self.work_book.save("analysis.xls")
	
	def __write(self):
		for x in range(len(self.subjects)):
			subject = self.subjects[x]
			self.sheet.write(0, 2 * x, subject.name.decode('utf-8'))
			for y in range(0, len(subject.datas)):
				self.sheet.write(y + 1, 2 * x, subject.datas[y])
		
		for x in range(len(self.rates)):
			rate = self.rates[x]
			self.sheet.write(0, 2 * x + 1, rate.name.decode('utf-8'))
			for y in range(0, len(subject.datas)):
				self.sheet.write(y + 1, 2 * x + 1, rate.datas[y])
		self.work_book.save("analysis.xls")
