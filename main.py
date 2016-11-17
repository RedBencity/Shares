# -*- coding: utf-8 -*-
from subject import *
from Rate import *
from shares_analysis import SharesAnalysis
from balancesheet import BalanceSheet

print "hello,world!"

# balance_sheet_name = raw_input("input balance_sheet_name : ")
balance_sheet_name = 'debtyear.xls'
subjects = list()
subjects.append(DateSubject("科目\时间"))
subjects.append(MoneySubject("资产总计"))
subjects.append(MoneySubject("货币资金"))
balance_sheet = BalanceSheet(balance_sheet_name, subjects)

for it in subjects:
	print it.name
	print it.datas
rates = list()
rates.append(OneRate("增长率", subjects[1]))
rates.append(TwoRate("增长率", subjects[1], subjects[2]))

analysis = SharesAnalysis(subjects, rates)
