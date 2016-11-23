class RequestRevision:
	''' Give revision filelist from server '''
	def __init__(self, server, revision):
		self.server = server
		self.revision = revision

	def act(self):
		return self.server.get(self.revision)
