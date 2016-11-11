from xml.sax.saxutils import escape


class Xml:
	def __init__(self, root_tag='root'):
		self.root_tag = root_tag
		self.content = []

	def write(self, **args):
		assert len(args) == 1
		k, v = args.popitem()
		self.content.append('<%s>' % k)
		if hasattr(v, 'print'):
			v.print(self)
		else:
			self.content.append(escape(str(v)))
		self.content.append('</%s>' % k)

	def xml(self):
		return '<?xml version="1.0"?><{0}>{1}</{0}>'.format(self.root_tag,
			''.join(self.content))
