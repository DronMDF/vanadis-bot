class IssueLocation:
	def __init__(self, file, line, position=None):
		self.file = file
		self.line = line
		self.position = position

	def __eq__(self, other):
		return all((self.file == other.file, self.line == other.line,
			self.position == other.position))

	def __repr__(self):
		if self.position is None:
			return 'IssueLocation("%s", %u)' % (self.file, self.line)
		return 'IssueLocation("%s", %u, %u)' % (self.file, self.line, self.position)

	def __str__(self):
		if self.position is None:
			return '%s:%u' % (self.file, self.line)
		return '%s:%u:%u' % (self.file, self.line, self.position)

	def print(self, stream):
		stream.write(file=self.file)
		stream.write(line=self.line)
		stream.write(position=self.position)
