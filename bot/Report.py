from . import IssueStream
from . import Xml


class File:
	def __init__(self, path, issues):
		self.path = path
		self.issues = issues

	def print(self, media):
		media.write(path=self.path)
		for i in self.issues:
			media.write(issue=i)


class Report:
	def __init__(self, instream):
		stream = IssueStream(instream)
		files = dict()
		for i in stream:
			if i.location.file not in files:
				files[i.location.file] = []
			files[i.location.file].append(i)

		request = Xml('files')
		for f, ii in files.items():
			file = File(f, ii)
			request.write(file=file)
		self.text = request.xml()

	def xml(self):
		return self.text
