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
time_range = (2015, 1991)
subjects_name = ["科目\时间", "资产总计", "股东权益合计", "营业总收入", "净利润"]
subjects = list()
subjects.append(DateSubject("科目\时间"))
for i in range(1, len(subjects_name)):
	subjects.append(MoneySubject(subjects_name[i]))

BalanceSheet(balance_sheet_name, subjects, time_range)
BenefitSheet(benefit_sheet_name, subjects,time_range)

for it in subjects:
	print it.name
	print it.datas

rates = list()
for i in range(1, len(subjects_name)):
	rates.append(OneRate("增长率", subjects[i]))

rates.append(TwoRate("货币资金/总资产", subjects[1], subjects[2]))
rates.append(TwoRate("净利润/股东权益合计", subjects[2], subjects[4]))
analysis = SharesAnalysis(subjects, rates)
