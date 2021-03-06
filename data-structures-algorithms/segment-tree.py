import math

class SegmentTree(object):

	def __init__(self, arr):
		self.arr = arr
		self.n = len(arr)
		st_height = math.ceil(math.log2(self.n))
		st_size = (2 * (2 ** st_height)) - 1
		self.st = [0]*st_size

	def constructHelper(self, st_start, st_end, st_index):
		if st_start == st_end:
			self.st[st_index] = self.arr[st_start]
			return self.st[st_index]
		
		mid = (st_start) + (st_end-st_start)//2

		self.st[st_index] =  min(self.constructHelper(st_start, mid, 2*st_index+1), \
			self.constructHelper(mid+1, st_end, 2*st_index+2))

		return self.st[st_index]

	def construct(self):
		self.constructHelper(0, self.n-1, 0)
		return self.st

	def queryHelper(self, st_start, st_end, q_start, q_end, st_index):
		if q_start <= st_start and q_end >= st_end:
			return self.st[st_index]
		
		if q_start > st_end or q_end < st_start:
			return float('inf')
		
		mid = (st_start) + (st_end-st_start)//2
		return min(self.queryHelper(st_start, mid, q_start, q_end, 2*st_index+1),\
			self.queryHelper(mid+1, st_end, q_start, q_end, 2*st_index+2))

	def query(self, q_start, q_end):
		if q_start > q_end or q_start < 0 or q_end >= self.n:
			return 'Error'
		return self.queryHelper(0, self.n-1, q_start, q_end, 0)





arr = [1, 3, 2, 7, 9, 11]  
st_obj = SegmentTree(arr)
st_obj.construct()
queries = [[0, 3], [2, 9], [2, 5]]
for [x, y] in queries:
	print(st_obj.query(x, y))
