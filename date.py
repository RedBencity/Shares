class Date:
	def __init__(self, begin, end):
		self.begin = begin
		self.end = end
		self.begin_offset = 0
		self.sub_date_length = 0
		self.max_sub_date_length = 0
		self.copy = []
	
	def calculate(self, datas):
		if len(self.copy) < len(datas):
			self.copy = []
			for data in datas:
				self.copy.append(data)
		
		self.begin_offset = 0
		self.sub_date_length = 0
		for i in range(1, len(datas)):
			time = int(repr(datas[i])[0:4])
			if time > self.begin:
				self.begin_offset += 1
			if self.end <= time:
				self.sub_date_length += 1
			if self.max_sub_date_length < self.sub_date_length:
				self.max_sub_date_length = self.sub_date_length
		return self.copy[
		       self.begin_offset + 1:self.max_sub_date_length + 1], self.begin_offset + 1, self.sub_date_length + 1
