from unittest import TestCase
from bot import Issue, IssueLocation


class TestIssue(TestCase):
	def testEquality(self):
		# Given
		a = Issue(IssueLocation('a.txt', 123, 321), 'test message')
		# Then
		self.assertEqual(a, Issue(IssueLocation('a.txt', 123, 321), 'test message'))
		self.assertNotEqual(a, Issue(IssueLocation('a.txt', 123, 321), 'test mexxage'))
		self.assertNotEqual(a, Issue(IssueLocation('b.txt', 123, 321), 'test message'))
		self.assertNotEqual(a, Issue(IssueLocation('a.txt', 123), 'test message'))
