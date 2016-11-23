import logging
from os.path import normpath
from xml.etree import ElementTree


class Filelist:
	def __init__(self, xml):
		root = ElementTree.fromstring(xml)
		self.paths = [e.text for e in root.findall('file/path')]

	def canonize(self, filename):
		fn = normpath(filename)
		for p in self.paths:
			if p.endswith(fn) or fn.endswith(p):
				return p
		logging.warning('No match filename %s', fn)
		return fn
