from unittest import TestCase
from bot import IssueLocation


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


class TestIssueLocation(TestCase):
	def testLocationEquality(self):
		# Given
		a = IssueLocation('a.txt', 123, 321)
		# Then
		self.assertEqual(a, IssueLocation('a.txt', 123, 321))
		self.assertNotEqual(a, IssueLocation('b.txt', 123, 321))
		self.assertNotEqual(a, IssueLocation('a.txt', 423, 321))
		self.assertNotEqual(a, IssueLocation('a.txt', 123, 521))
		self.assertNotEqual(a, IssueLocation('a.txt', 123))

	def testPrintToStream(self):
		# Given
		stream = DataStream()
		location = IssueLocation('a.txt', 123, 321)
		# When
		location.print(stream)
		# Then
		self.assertListEqual(stream.data,
			[('file', 'a.txt'), ('line', 123), ('position', 321)])

	def testPrintToStreamWithoutPosition(self):
		# Given
		stream = DataStream()
		location = IssueLocation('b.txt', 777)
		# When
		location.print(stream)
		# Then
		self.assertListEqual(stream.data, [('file', 'b.txt'), ('line', 777)])
