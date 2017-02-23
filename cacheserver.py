class cacheserver(object):
	def __init__(self, idx, capacity):
		self.id = idx 
		self.capacity = capacity
		self.videosid = [] #contains videos
	

	def addvideo(self, videoid):
		return 0

	def testcapacity(self, video):
		#tester capacité: tester si cache a assez de place pour video
		return booleen