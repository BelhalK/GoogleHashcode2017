import numpy as np

class request(object):
	def __init__(self, endpointid, videoid, value):
		self.endpoint = endpointid
		self.video = videoid
		self.value = value
		
