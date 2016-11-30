# -*- coding: utf-8 -*-
from subject import *
from rate import *
from shares_analysis import SharesAnalysis
from finance_sheet import *
from  date import *

print "hello,world!"

# balance_sheet_name = raw_input("input balance_sheet_name : ")
balance_sheet_name = 'debtyear.xls'
benefit_sheet_name = 'benefityear.xls'
cash_sheet_name = 'cashyear.xls'
time_range = Date(2015, 2006)
subjects_name = ["科目\时间", "资产总计", "归属于母公司股东权益合计", "营业总收入", "净利润", "扣非净利润", "经营现金流量净额"]
subjects = list()
subjects.append(DateSubject("科目\时间"))
for i in range(1, len(subjects_name)):
	subjects.append(MoneySubject(subjects_name[i]))

BalanceSheet(balance_sheet_name, subjects, time_range)
BenefitSheet(benefit_sheet_name, subjects, time_range)
CashSheet(cash_sheet_name, subjects, time_range)

for it in subjects:
	print it.name
	print it.datas

rates = list()
for i in range(1, len(subjects_name)):
	rates.append(OneRate("增长率", subjects[i]))

rates.append(TwoRate("股东权益合计/资产总计", subjects[2], subjects[1]))
rates.append(TwoRate("净资产收益率", subjects[4], subjects[2]))
analysis = SharesAnalysis(subjects, rates)
