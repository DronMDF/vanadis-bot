from unittest import TestCase
from bot import RequestImport
from test import FakeServer


class TestRequestPost(TestCase):
	def testUrlFormer(self):
		# Given
		server = FakeServer()
		revision = '1234567'
		data = 'test data'
		request = RequestImport(server, revision, data)
		# When
		request.act()
		# Then
		self.assertEqual(server.method, 'POST')
		self.assertEqual(server.url, 'import/' + revision)
		self.assertEqual(server.data, data)
