# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Rate(object):
	def __init__(self, name, subjects_list):
		self.name = name
		self.subjects_list = subjects_list
	
	@abstractmethod
	def calculate(self):
		pass


class OneRate(Rate):
	def __init__(self, name, subjects):
		super(OneRate, self).__init__(name, subjects)
		self.datas = []
	
	def calculate(self):
		original_datas = self.subjects_list.datas
		for i in range(len(original_datas)):
			if i < len(original_datas) - 1:
				if original_datas[i + 1] == 0:
					data = 0
					data = round(data, 2)
				else:
					data = (original_datas[i] - original_datas[i + 1]) / original_datas[i + 1]
					data = round(data, 2)
				self.datas.append(data)
			else:
				self.datas.append(0)
		print self.datas


class TwoRate(Rate):
	def __init__(self, name, *subjects_list):
		super(TwoRate, self).__init__(name, subjects_list)
		self.datas = []
	
	def calculate(self):
		first_original_datas = self.subjects_list[0].datas
		second_original_datas = self.subjects_list[1].datas
		print first_original_datas
		print second_original_datas
		for i in range(max(len(first_original_datas), len(second_original_datas))):
			data = second_original_datas[i] / first_original_datas[i]
			data = round(data, 2)
			self.datas.append(data)
