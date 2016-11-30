from . import IssueStream
from . import Xml


class File:
	def __init__(self, oid, issues):
		self.id = oid
		self.issues = issues

	def print(self, media):
		media.write(id=self.id)
		for i in self.issues:
			media.write(issue=i)


class Report:
	def __init__(self, instream, filelist):
		stream = IssueStream(instream)
		files = dict()
		for i in stream:
			filename = filelist.canonize(i.location.file)
			if filename not in files:
				files[filename] = []
			files[filename].append(i)

		request = Xml('files')
		for f, ii in files.items():
			file = File(filelist.fileid(f), ii)
			request.write(file=file)
		self.text = request.xml()

	def xml(self):
		return self.text
