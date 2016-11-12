class Issue:
	def __init__(self, location, message):
		self.location = location
		self.message = message

	def __eq__(self, other):
		return all((self.location == other.location, self.message == other.message))

	def __repr__(self):
		return 'Issue(%s, "%s")' % (repr(self.location), self.message)

	def __str__(self):
		return '%s: %s' % (self.location, self.message)

	def print(self, stream):
		stream.write(line=self.location.line)
		if self.location.position is not None:
			stream.write(position=self.location.position)
		stream.write(message=self.message)
