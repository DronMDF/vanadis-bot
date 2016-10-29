import re
from . import Issue, IssueLocation


class IssueStream:
	def __init__(self, stream):
		self.stream = stream

	def __iter__(self):
		return self

	def __next__(self):
		for rl in self.stream:
			m1 = re.match(r'^(.*):(\d+):(\d+): (warning: .*)$', rl)
			if m1:
				location = IssueLocation(m1.group(1), int(m1.group(2)),
					int(m1.group(3)))
				return Issue(location, m1.group(4))
			m2 = re.match((r'^\[(.*?):(\d+)\].*: '
				r'\((error|warning|performance|style)\) (.*)$'), rl)
			if m2:
				location = IssueLocation(m2.group(1), int(m2.group(2)))
				return Issue(location, m2.group(3) + ': ' + m2.group(4))
		raise StopIteration
