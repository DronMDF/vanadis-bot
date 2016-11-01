from unittest import TestCase
from bot import Issue, IssueLocation
from test import DataStream


class TestIssue(TestCase):
	def testEquality(self):
		# Given
		a = Issue(IssueLocation('a.txt', 123, 321), 'test message')
		# Then
		self.assertEqual(a, Issue(IssueLocation('a.txt', 123, 321), 'test message'))
		self.assertNotEqual(a, Issue(IssueLocation('a.txt', 123, 321), 'test mexxage'))
		self.assertNotEqual(a, Issue(IssueLocation('b.txt', 123, 321), 'test message'))
		self.assertNotEqual(a, Issue(IssueLocation('a.txt', 123), 'test message'))

	def testPrintToStream(self):
		# Given
		stream = DataStream()
		issue = Issue(IssueLocation('a.txt', 123), 'msg')
		# When
		issue.print(stream)
		# Then
		self.assertListEqual(stream.data,
			[('location', [('file', 'a.txt'), ('line', 123)]), ('message', 'msg')])
