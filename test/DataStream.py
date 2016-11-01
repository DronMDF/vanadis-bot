class DataStream:
	def __init__(self):
		self.data = []

	def write(self, **args):
		assert len(args) == 1
		k, v = args.popitem()
		if hasattr(v, 'print'):
			ss = DataStream()
			v.print(ss)
			value = ss.data
		else:
			value = v
		self.data.append((k, value))
