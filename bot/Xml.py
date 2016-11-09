class Xml:
	def __init__(self, root_tag='root'):
		self.root_tag = root_tag

	def xml(self):
		return '<?xml version="1.0"?><{0}></{0}>'.format(self.root_tag)
