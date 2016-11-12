from io import StringIO
from unittest import TestCase
from bot import Issue, IssueStream, IssueLocation


class TestInputStream(TestCase):
	def testParseClangIssue(self):
		# Given
		stream = StringIO('pid_output.c:101:30: warning: implicit conversion')
		issue_stream = IssueStream(stream)
		# When
		issue = next(issue_stream)
		# Then
		self.assertEqual(issue, Issue(IssueLocation('pid_output.c', 101, 30),
					'warning: implicit conversion'))
