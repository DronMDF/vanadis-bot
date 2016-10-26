from unittest import TestCase
from bot import IssueLocation


class TestIssueLocation(TestCase):
	def testLocationEquality(self):
		# Given
		a = IssueLocation('a.txt', 123, 321)
		# Then
		self.assertEqual(a, IssueLocation('a.txt', 123, 321))
		self.assertNe(a, IssueLocation('b.txt', 123, 321))
		self.assertNe(a, IssueLocation('a.txt', 423, 321))
		self.assertNe(a, IssueLocation('a.txt', 123, 521))
		self.assertNe(a, IssueLocation('a.txt', 123))
