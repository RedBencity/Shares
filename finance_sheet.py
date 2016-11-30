# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
import xlrd


class FinanceSheet(object):
	def __init__(self, file_name, subjects, time_range):
		self.file_name = file_name
		self.subjects = subjects
		self.time_range = time_range
		self.__sheet_data = None
		self.__init_sheet()
		self.__parse_sheet()
	
	def __init_sheet(self):
		self.__sheet_data = xlrd.open_workbook(self.file_name)
	
	def __parse_sheet(self):
		print "begin parse sheet !"
		table = self.__sheet_data.sheets()[0]
		
		self.subjects[0].datas = table.row_values(0)
		self.subjects[0].convert_unit()
		
		self.subjects[0].datas, begin_offset, sub_date_length = self.time_range.calculate(self.subjects[0].datas)
		for i in range(1, table.nrows):
			name = table.col_values(0)[i]
			if isinstance(name, unicode):
				name = name.encode('utf-8')
			for j in range(1, len(self.subjects)):
				if name == self.subjects[j].name:
					self.subjects[j].datas = table.row_values(i)[begin_offset:sub_date_length]
					self.subjects[j].convert_unit()


class BalanceSheet(FinanceSheet):
	def __init__(self, file_name, subjects, time_range):
		super(BalanceSheet, self).__init__(file_name, subjects, time_range)


class BenefitSheet(FinanceSheet):
	def __init__(self, file_name, subjects, time_range):
		super(BenefitSheet, self).__init__(file_name, subjects, time_range)


class CashSheet(FinanceSheet):
	def __init__(self, file_name, subjects, time_range):
		super(CashSheet, self).__init__(file_name, subjects, time_range)
