from unittest import TestCase
from bot import RequestRevision
from test import FakeServer


class TestRequestRevision(TestCase):
	def testUrlFormer(self):
		# Given
		server = FakeServer()
		revision = '1234567'
		request = RequestRevision(server, revision)
		# When
		request.act()
		# Then
		self.assertEqual(server.method, 'GET')
		self.assertEqual(server.url, revision)
