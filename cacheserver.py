import video

class cacheserver(object):
	def __init__(self, idx, capacity):
		self.idx = idx 
		self.capacity = capacity
		self.videosid = [] #contains videos
	

	def addvideo(self, videoid):
		self.videosid.append(videoid)
		return 0

	def updatecapacity(self):
		self.capacity = 0
		for video in self.videosid:
			self.capacity =  self.capacity + videosid.size
		return 0

	def testcapacity(self, video):
		#tester capacité: tester si cache a assez de place pour video
		if self.capacity 
		return booleen