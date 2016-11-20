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
		
		subject = self.subjects[0]
		self.sheet.write(0, 0, subject.name.decode('utf-8'))
		for y in range(0, len(subject.datas)):
			self.sheet.write(y + 1, 0, subject.datas[y])
		
		for x in range(1, len(self.subjects)):
			subject = self.subjects[x]
			self.sheet.write(0, 2 * x - 1, subject.name.decode('utf-8'))
			for y in range(0, len(subject.datas)):
				self.sheet.write(y + 1, 2 * x - 1, subject.datas[y])
		
		style = XFStyle()
		style.num_format_str = '0.00%'
		row = len(self.subjects)
		for x in range(len(self.rates)):
			rate = self.rates[x]
			if x < row:
				self.sheet.write(0, 2 * x + 2, rate.name.decode('utf-8'))
				for y in range(0, len(rate.datas)):
					self.sheet.write(y + 1, 2 * x + 2, rate.datas[y], style)
			else:
				self.sheet.write(0, row + x, rate.name.decode('utf-8'))
				for y in range(0, len(rate.datas)):
					self.sheet.write(y + 1, row + x, rate.datas[y], style)
		self.work_book.save("analysis.xls")
