# -*- coding: utf-8 -*-

import xlrd
from subject import *


class BalanceSheet:
	__sheet_data = None
	
	def __init__(self, file_name, subjects):
		self.file_name = file_name
		self.subjects = subjects
		self.__init_sheet()
		self.__parse_sheet()
	
	def __init_sheet(self):
		self.__sheet_data = xlrd.open_workbook(self.file_name)
	
	def __parse_sheet(self):
		print "begin parse balance sheet !"
		table = self.__sheet_data.sheets()[0]
		for i in range(table.nrows):
			name = table.col_values(0)[i]
			if isinstance(name, unicode):
				name = name.encode('utf-8')
			for j in range(len(self.subjects)):
				if name == self.subjects[j].name:
					self.subjects[j].datas = table.row_values(i)[1:]
					self.subjects[j].convert_unit()
