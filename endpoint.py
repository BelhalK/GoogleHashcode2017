class endpoint(object):
	def __init__(self,idx, latency_datacenter):
		self.idx = idx 
		self.cacheservers = [] #contains cacheservers ids, latencies
		self.latency_datacenter = latency_datacenter

	def addcacheserver(self, cacheserverid):
		self.cacheservers+=[cacheserverid]

	def findbestcache(self, videoid, videos, listcacheserver):
		#tester trouve la meilleure latency possible (capacité et connectivité)
		L=latency_datacenter
		bestCacheserverId=-1
		for c in cacheservers:
			if listofcacheservers[c[0]].can_add_video_or_video_already_in(videoid,videos):
				if c[1]>L:
					L=c[1]
					cacheserverId=c[0]
		return L,cacheserverId
	
	def getcurrentlatency(self, videoid, listcacheservers):
		#calcule la latency actuel pour la videoid
		L=latency_datacenter
		cacheserverId=-1
		for c in self.cacheservers:
			if listofcacheservers[c[0]].isvideoinside(videoid):
				if c[1]>L:
					L=c[1]
					cacheserverId=c[0]
		return L,cacheserverId
