class endpoint(object):
	def __init__(self,idx, latency_datacenter,):
		self.id = idx 
		self.cacheservers = [] #contains cacheservers ids, latencies
		self.latency_datacenter = latency_datacenter

	
	def :