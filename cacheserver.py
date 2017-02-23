import video

class cacheserver(object):
	def __init__(self, idx, capacity):
		self.idx = idx 
		self.capacity = capacity
		self.videosid = [] #contains videos
	

	def addvideo(self, videoid,videos):
		# retourne true et addla video si y a de la place
		# sinon retourne false
		if self.capacity-videos[videoid].size>=0:
			self.capacity-=videos[videoid].size
			self.videosid.append(videoid)
			return True
		else:
			return False

	def isvideoinside(self,videoid):
		return videoid in self.videosid

	def can_add_video_or_video_already_in(self,videoid,videos):
		b=(videoid in self.videosid)
		if b==True:
			return b
		else:
			return self.capacity-videos[videoid].size>=0