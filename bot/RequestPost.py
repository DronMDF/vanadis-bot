class RequestPost:
	def __init__(self, server, url, data):
		self.server = server
		self.url = url
		self.data = data

	def act(self):
		return self.server.post(self.url, self.data)
