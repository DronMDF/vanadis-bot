import logging
from time import perf_counter


class Timer:
	def __init__(self):
		self.start = None
		self.interval = None

	def __enter__(self):
		self.start = perf_counter()
		return self

	def __exit__(self, *args):
		self.interval = perf_counter() - self.start
		return False


class RequestLogTime:
	def __init__(self, request):
		self.request = request

	def act(self):
		with Timer() as t:
			reply = self.request.act()
		logging.info('Server request take a %ums', int(t.interval * 1000))
		return reply
