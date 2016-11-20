# -*- coding: utf-8 -*-
from subject import *
from Rate import *
from shares_analysis import SharesAnalysis
from balance_sheet import BalanceSheet
from benefit_sheet import BenefitSheet

print "hello,world!"

# balance_sheet_name = raw_input("input balance_sheet_name : ")
balance_sheet_name = 'debtyear.xls'
benefit_sheet_name = 'benefityear.xls'
subjects = list()
subjects.append(DateSubject("科目\时间"))
subjects.append(MoneySubject("资产总计"))
subjects.append(MoneySubject("货币资金"))
subjects.append(MoneySubject("股东权益合计"))
subjects.append(MoneySubject("营业总收入"))
subjects.append(MoneySubject("净利润"))
BalanceSheet(balance_sheet_name, subjects)
BenefitSheet(benefit_sheet_name, subjects)
for it in subjects:
	print it.name
	print it.datas

rates = list()
rates.append(OneRate("增长率", subjects[1]))
rates.append(OneRate("增长率", subjects[2]))
rates.append(OneRate("增长率", subjects[3]))
rates.append(OneRate("增长率", subjects[4]))
rates.append(OneRate("增长率", subjects[5]))
# rates.append(TwoRate("货币资金/总资产", subjects[1], subjects[2]))
# rates.append(TwoRate("净利润/股东权益合计", subjects[1], subjects[2]))
analysis = SharesAnalysis(subjects, rates)
