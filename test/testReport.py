from io import StringIO
from unittest import TestCase
from bot import Report


class FakeFilelist:
	def canonize(self, filename):		# pylint: disable=unused-argument
		return 'common/pid_output.c'


class TestReport(TestCase):
	def testSimpleReport(self):
		# Given
		stream = StringIO('pid_output.c:101:30: warning: implicit conversion')
		# When
		report = Report(stream, FakeFilelist())
		# Then
		expected = ('<file><path>common/pid_output.c</path><issue><line>101</line>'
			'<position>30</position><message>warning: '
			'implicit conversion</message></issue></file>')
		self.assertIn(expected, report.xml())
