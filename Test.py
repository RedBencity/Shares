class Test:
	datas = []
	data = 1
	
	def __init__(self):
		self.aaa = []
	
	def test(self):
		self.datas.append("aaa")


test1 = Test()
# test1.test()
# print test1.datas
print "--------------------------"
print test1.data
print id(test1.data)
print id(Test.data)
print "--------------------------"
Test.data = 2
print id(Test.data)
print id(test1.data)
print test1.data
print "--------------------------"
test2 = Test()
print test2.data
print id(test2.data)
test2.data = 3
# test2.test()
Test.data = 4
# print test1.datas
# print test2.datas
print Test.data
print test1.data
print test2.data
print "---------------------------"
test3 = Test()
test3.datas = []

test4 = Test()
print id(test3.data)

print id(test4.data)

print id(test3.datas)
print id(test4.datas)
print id(test3.aaa)
print id(test4.aaa)
