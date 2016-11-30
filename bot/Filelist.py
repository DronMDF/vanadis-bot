import logging
from os.path import normpath
from xml.etree import ElementTree


class Filelist:
	def __init__(self, xml):
		root = ElementTree.fromstring(xml)
		self.paths = {f.findtext('path'): f.findtext('id') for f in root.findall('file')}

	def canonize(self, filename):
		fn = normpath(filename)
		for p in self.paths.keys():
			if p.endswith(fn) or fn.endswith(p):
				return p
		logging.warning('No match filename %s', fn)
		return fn

	def fileid(self, filename):
		return self.paths[filename]
