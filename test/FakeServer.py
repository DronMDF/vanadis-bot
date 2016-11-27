class FakeServer:
	def __init__(self):
		self.method = None
		self.url = None
		self.data = None

	def get(self, url):
		self.method = 'GET'
		self.url = url

	def post(self, url, data):
		self.method = 'POST'
		self.url = url
		self.data = data
