class endpoint(object):
	def __init__(self,idx, latency_datacenter,):
		self.id = idx 
		self.cacheservers = [] #contains cacheservers ids, latencies
		self.latency_datacenter = latency_datacenter

	def addcacheserver(self, cacheserver):
		return 0

	def findbestcache(self, videoid, listcacheserver):
		#tester trouve la meilleure latency possible (capacité et connectivité)
		return cacheserverid,latency
	
	def getcurrentlatency(self, videoid):
		#calcule la latency actuel pour la videoid
		return latency
