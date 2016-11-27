class RequestImport:
	def __init__(self, server, revision, data):
		self.server = server
		self.revision = revision
		self.data = data

	def act(self):
		return self.server.post('import/' + self.revision, self.data)
