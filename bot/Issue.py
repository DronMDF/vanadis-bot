class Issue:
	def __init__(self, location, message):
		self.location = location
		self.message = message

	def __eq__(self, other):
		return (self.location, self.message) == (other.location, other.message)

	def print(self, stream):
		stream.write(location=self.location)
		stream.write(message=self.message)
